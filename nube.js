/* Cuentas en la nube (Firebase): acceso, aprobación por un administrador y progreso sincronizado.
   Se carga antes del script principal; usa sus variables globales (usuario, estado, ruta, guardar...) solo al ejecutarse. */
"use strict";
const Nube = {
  api: null, activo: false, authListo: false, admin: false, perfil: null, acceso: null, uid: null,
  nombreNuevo: "", modoRegistro: false, timer: null, pendientes: 0,

  /* ---------- arranque ---------- */
  async iniciar() {
    const r = await window.FB_READY;
    if (!r) return false;                                   // sin configurar -> perfiles locales
    this.activo = true;
    this.construir();
    if (r === "fallo") { this.sinConexion(); return true; }
    this.api = r;
    this.api.onAuth(u => this.cambioAuth(u));
    return true;
  },

  sinConexion() {
    this.authListo = true;
    let ult = null;
    try { ult = JSON.parse(lsGet("entzun-ultimo") || "null"); } catch (e) {}
    if (ult) { this.entrarLocal(ult.uid, ult.nombre); return; }
    this.acceso = null;
    this.mostrarError("No hay conexión. Conéctate a internet para entrar la primera vez.");
    location.hash = "#/entrar"; ruta();
  },
  entrarLocal(uid, nombre) {
    usuario = { id: uid, nombre, color: this.colorDe(uid) };
    cargarEstado(); this.acceso = "aprobado";
    const ult = eps.find(e => k(e) === estado.actual && disp(e)); if (ult) cargar(ult, false);
    if (/^#\/(entrar|pendiente)$/.test(location.hash)) location.hash = "#/";
    ruta();
  },
  colorDe(uid) { let h = 0; for (const c of uid) h = (h * 31 + c.charCodeAt(0)) >>> 0; return COLORES_USUARIO[h % COLORES_USUARIO.length]; },

  /* ---------- sesión ---------- */
  async cambioAuth(u) {
    if (!u) {
      this.authListo = true;
      this.uid = null; this.admin = false; this.perfil = null; this.acceso = null;
      audio.pause(); audio.removeAttribute("src"); cur = null; $("mini").classList.remove("on");
      usuario = null; estado = VACIO();
      lsDel("entzun-ultimo");
      if (this.modoRegistro) this.alternar();
      this.nombreNuevo = ""; $("e-nombre").value = ""; $("e-clave").value = ""; this.mostrarError("");
      location.hash = "#/entrar"; ruta(); return;
    }
    this.uid = u.uid;
    try {
      let p = await this.api.perfil(u.uid);
      if (!p) { await this.api.crearPerfil(u, this.nombreNuevo); p = await this.api.perfil(u.uid); }
      this.admin = await this.api.esAdmin(u.uid);
      if (this.admin && p.estado !== "aprobado") { await this.api.cambiarEstado(u.uid, "aprobado"); p.estado = "aprobado"; }
      this.perfil = p; this.acceso = p.estado; lsSet("entzun-nube", "1"); this.authListo = true;
      if (p.estado === "aprobado") await this.activar(u, p); else { usuario = null; this.pintarEspera(p); location.hash = "#/pendiente"; ruta(); }
    } catch (e) {
      this.authListo = true;
      let ult = null; try { ult = JSON.parse(lsGet("entzun-ultimo") || "null"); } catch (_) {}
      if (ult && ult.uid === u.uid) { this.entrarLocal(ult.uid, ult.nombre); return; }
      this.mostrarError("No se pudo comprobar tu cuenta. Revisa la conexión e inténtalo otra vez.");
      location.hash = "#/entrar"; ruta();
    }
  },

  // La primera cuenta que entra en este móvil hereda el perfil local, si solo hay uno (con varios no se sabe de quién es).
  heredarPerfilLocal() {
    if (lsGet("entzun-heredado") || lsGet(claveEstado(usuario))) return;
    let locales = []; try { locales = JSON.parse(lsGet(U_KEY) || "[]"); } catch (e) {}
    const viejo = locales.length === 1 && lsGet(claveEstado(locales[0]));
    if (viejo) { lsSet(claveEstado(usuario), viejo); lsSet("entzun-heredado", "1"); }
  },

  async activar(u, p) {
    usuario = { id: u.uid, nombre: p.nombre || u.displayName || (u.email || "").split("@")[0], color: this.colorDe(u.uid) };
    lsSet("entzun-ultimo", JSON.stringify({ uid: u.uid, nombre: usuario.nombre }));
    this.heredarPerfilLocal();
    cargarEstado();
    try {                                                  // se queda el progreso más reciente (nube o este móvil)
      const r = await this.api.leerProgreso(u.uid);
      if (r) { const re = JSON.parse(r.estado); if ((re.actualizado || 0) > (estado.actualizado || 0)) { estado = Object.assign(VACIO(), mig(re)); lsSet(claveEstado(usuario), JSON.stringify(estado)); } }
    } catch (e) {}
    const ult = eps.find(x => k(x) === estado.actual && disp(x)); if (ult) cargar(ult, false);
    if (/^#\/(entrar|pendiente)$/.test(location.hash) || !location.hash) location.hash = "#/";
    ruta();
    if (this.admin) this.contarPendientes();
  },

  subir() {
    if (!this.api || !usuario) return;
    clearTimeout(this.timer);
    this.timer = setTimeout(() => this.api.guardarProgreso(usuario.id, estado).catch(() => {}), 1500);
  },

  guardia(h) {                                               // devuelve el hash al que hay que ir, o null si está bien
    if (!usuario) {
      if (h === "#/entrar" || h === "#/pendiente") return h === "#/pendiente" && !this.acceso ? "#/entrar" : null;
      return this.acceso === "pendiente" || this.acceso === "bloqueado" ? "#/pendiente" : "#/entrar";
    }
    if (h === "#/entrar" || h === "#/pendiente") return "#/";
    if (h === "#/admin" && !this.admin) return "#/";
    return null;
  },

  /* ---------- pantallas ---------- */
  construir() {
    if ($("vista-entrar")) return;
    const cont = document.createElement("div");
    cont.innerHTML = `
<div id="vista-entrar" class="oculto"><div class="pad">
  <h1>Entzun</h1>
  <p class="ayuda" id="e-ayuda">Entra con tu cuenta para escuchar y guardar tu progreso.</p>
  <input id="e-nombre" type="text" class="campo oculto" maxlength="30" placeholder="Tu nombre" autocomplete="name" autocapitalize="words" aria-label="Tu nombre">
  <input id="e-correo" type="email" class="campo" placeholder="Correo electrónico" autocomplete="email" autocapitalize="off" aria-label="Correo electrónico">
  <input id="e-clave" type="password" class="campo" placeholder="Contraseña" autocomplete="current-password" aria-label="Contraseña">
  <div id="e-error" class="error" role="alert"></div>
  <button id="e-enviar" class="btn-verde">Entrar</button>
  <button id="e-google" class="btn-sec">Entrar con Google</button>
  <button id="e-cambiar" class="enlace">¿No tienes cuenta? Crear cuenta</button>
  <button id="e-olvide" class="enlace">He olvidado mi contraseña</button>
</div></div>

<div id="vista-pendiente" class="oculto"><div class="pad">
  <h1 id="p-tit">Cuenta pendiente</h1>
  <p class="ayuda" id="p-txt"></p>
  <button id="p-otra" class="btn-verde">Comprobar otra vez</button>
  <button id="p-salir" class="btn-sec">Salir</button>
</div></div>

<div id="vista-cuenta" class="oculto"><div class="pad">
  <button id="c-atras" class="atras" aria-label="Volver"><svg viewBox="0 0 24 24"><path d="M15.4 7.4 14 6l-6 6 6 6 1.4-1.4L10.8 12z"/></svg></button>
  <div class="avatar grande" id="c-avatar"></div>
  <h1 id="c-nombre" style="margin-top:12px"></h1>
  <p class="ayuda" id="c-correo"></p>
  <button id="c-admin" class="btn-verde oculto">Gestionar usuarios</button>
  <button id="c-salir" class="btn-sec">Cerrar sesión</button>
</div></div>

<div id="vista-admin" class="oculto"><div class="pad">
  <button id="a-atras" class="atras" aria-label="Volver"><svg viewBox="0 0 24 24"><path d="M15.4 7.4 14 6l-6 6 6 6 1.4-1.4L10.8 12z"/></svg></button>
  <h1>Usuarios</h1>
  <p class="ayuda">Aprueba a quien quieras que use Entzun. Los nuevos aparecen como pendientes.</p>
  <div id="a-lista"></div>
</div></div>`;
    const ref = $("aviso");
    while (cont.firstChild) ref.parentNode.insertBefore(cont.firstChild, ref);

    const css = document.createElement("style");
    css.textContent = `
.campo{width:100%;font:600 22px/1.2 inherit;font-family:inherit;color:#fff;background:var(--fila);border:2px solid var(--linea);border-radius:14px;padding:16px;margin:0 0 12px}
.campo:focus{outline:none;border-color:var(--verde)}
.error{color:var(--mal-suave);font-size:19px;font-weight:600;min-height:26px;margin:0 0 10px}
.enlace{display:block;width:100%;color:var(--verde);font-size:20px;font-weight:700;min-height:56px}
.atras{width:64px;height:64px;display:grid;place-items:center;margin-left:-14px}.atras svg{width:34px;height:34px}
.avatar.grande{width:96px;height:96px;font-size:44px}
.fila-u{background:var(--fila);border-radius:14px;padding:14px;margin-bottom:12px}
.fila-u .n{font-size:22px;font-weight:700}.fila-u .c{color:var(--suave);font-size:17px;word-break:break-all}
.fila-u .e{font-size:17px;font-weight:700;margin:6px 0 10px}
.e.pendiente{color:#ffb74d}.e.aprobado{color:var(--verde)}.e.bloqueado{color:var(--mal-suave)}
.fila-u .b{display:flex;gap:10px}.fila-u .b button{flex:1;min-height:56px;border-radius:30px;font-weight:700;font-size:19px;background:var(--fila2)}
.fila-u .b .si{background:var(--verde);color:#000}
#aviso-admin{margin:0 var(--lado) 12px;background:#4a3b12;border-radius:14px;padding:16px 18px;display:none;width:calc(100% - 2 * var(--lado));text-align:left;font-size:20px;font-weight:700}
#aviso-admin.on{display:block}`;
    document.head.appendChild(css);

    const aa = document.createElement("button"); aa.id = "aviso-admin";
    $("instalar").parentNode.insertBefore(aa, $("instalar"));
    aa.onclick = () => { location.hash = "#/admin"; };

    $("e-enviar").onclick = () => this.enviar();
    $("e-google").onclick = () => this.google();
    $("e-cambiar").onclick = () => this.alternar();
    $("e-olvide").onclick = () => this.olvide();
    for (const id of ["e-correo", "e-clave", "e-nombre"]) $(id).addEventListener("keydown", e => { if (e.key === "Enter") this.enviar(); });
    $("p-otra").onclick = () => location.reload();
    $("p-salir").onclick = () => this.salir();
    $("c-atras").onclick = () => { location.hash = "#/"; };
    $("c-salir").onclick = () => this.salir();
    $("c-admin").onclick = () => { location.hash = "#/admin"; };
    $("a-atras").onclick = () => { location.hash = "#/cuenta"; };
  },

  alternar() {
    this.modoRegistro = !this.modoRegistro;
    const r = this.modoRegistro;
    $("e-nombre").classList.toggle("oculto", !r);
    $("e-enviar").textContent = r ? "Crear cuenta" : "Entrar";
    $("e-google").textContent = r ? "Registrarme con Google" : "Entrar con Google";
    $("e-cambiar").textContent = r ? "¿Ya tienes cuenta? Entrar" : "¿No tienes cuenta? Crear cuenta";
    $("e-clave").autocomplete = r ? "new-password" : "current-password";
    $("e-ayuda").textContent = r ? "Crea tu cuenta. Después, el administrador tendrá que aprobarla para que puedas entrar." : "Entra con tu cuenta para escuchar y guardar tu progreso.";
    this.mostrarError("");
  },
  mostrarError(t) { const e = $("e-error"); if (e) e.textContent = t || ""; },
  traducir(e) {
    const c = (e && e.code) || "";
    if (c === "auth/popup-closed-by-user" || c === "auth/cancelled-popup-request") return "";
    if (c === "auth/invalid-email") return "El correo no es válido.";
    if (["auth/user-not-found", "auth/wrong-password", "auth/invalid-credential"].includes(c)) return "Correo o contraseña incorrectos.";
    if (c === "auth/email-already-in-use") return "Ese correo ya tiene cuenta. Pulsa «Entrar».";
    if (c === "auth/weak-password") return "La contraseña debe tener al menos 6 caracteres.";
    if (c === "auth/network-request-failed") return "Sin conexión. Inténtalo otra vez.";
    if (c === "auth/too-many-requests") return "Demasiados intentos. Espera un momento.";
    if (c === "auth/unauthorized-domain") return "Esta dirección no está autorizada en Firebase (ver FIREBASE.md).";
    return "No se pudo entrar. Inténtalo de nuevo.";
  },
  async enviar() {
    if (!this.api) { this.mostrarError("No hay conexión con el servidor."); return; }
    const correo = $("e-correo").value.trim(), clave = $("e-clave").value, nombre = $("e-nombre").value.trim();
    if (!correo || !clave) { this.mostrarError("Escribe tu correo y tu contraseña."); return; }
    if (this.modoRegistro && !nombre) { this.mostrarError("Escribe tu nombre."); return; }
    this.mostrarError(""); $("e-enviar").disabled = true;
    try {
      if (this.modoRegistro) { this.nombreNuevo = nombre; await this.api.registrar(correo, clave); }
      else await this.api.entrar(correo, clave);
      $("e-clave").value = "";
    } catch (e) { this.mostrarError(this.traducir(e)); }
    $("e-enviar").disabled = false;
  },
  async google() {
    if (!this.api) { this.mostrarError("No hay conexión con el servidor."); return; }
    this.mostrarError("");
    try { if (this.modoRegistro) this.nombreNuevo = $("e-nombre").value.trim(); await this.api.google(); }
    catch (e) { this.mostrarError(this.traducir(e)); }
  },
  async olvide() {
    const correo = $("e-correo").value.trim();
    if (!correo) { this.mostrarError("Escribe tu correo arriba y vuelve a pulsar."); return; }
    try { await this.api.recuperar(correo); this.mostrarError(""); alert("Te hemos enviado un correo para cambiar la contraseña."); }
    catch (e) { this.mostrarError(this.traducir(e)); }
  },
  async salir() { try { if (this.api) await this.api.salir(); else { lsDel("entzun-ultimo"); location.reload(); } } catch (e) {} },

  pintarEspera(p) {
    $("p-tit").textContent = p.estado === "bloqueado" ? "Acceso no permitido" : "Cuenta pendiente";
    $("p-txt").textContent = p.estado === "bloqueado"
      ? "El administrador no ha permitido el acceso con esta cuenta."
      : "Tu cuenta está creada, pero el administrador todavía tiene que aprobarla. Cuando lo haga, pulsa «Comprobar otra vez».";
  },
  pintarCuenta() {
    if (!usuario) return;
    const av = $("c-avatar"); av.style.background = usuario.color; av.textContent = inicial(usuario);
    $("c-nombre").textContent = usuario.nombre;
    $("c-correo").textContent = (this.perfil && this.perfil.email) || "";
    $("c-admin").classList.toggle("oculto", !this.admin);
    if (this.admin) this.contarPendientes().then(n => { $("c-admin").textContent = n ? `Gestionar usuarios (${n} pendientes)` : "Gestionar usuarios"; });
  },

  /* ---------- administración ---------- */
  async contarPendientes() {
    if (!this.admin || !this.api) return 0;
    try { this.pendientes = (await this.api.listarUsuarios()).filter(u => u.estado === "pendiente").length; } catch (e) { this.pendientes = 0; }
    this.pintarAviso(); return this.pendientes;
  },
  pintarAviso() {
    const a = $("aviso-admin"); if (!a) return;
    a.classList.toggle("on", this.admin && this.pendientes > 0);
    a.textContent = this.pendientes === 1 ? "1 persona espera tu aprobación" : `${this.pendientes} personas esperan tu aprobación`;
  },
  async pintarAdmin() {
    const l = $("a-lista"); l.innerHTML = '<p class="ayuda">Cargando…</p>';
    let us = [];
    try { us = await this.api.listarUsuarios(); } catch (e) { l.innerHTML = '<p class="ayuda">No se pudo cargar la lista.</p>'; return; }
    const orden = { pendiente: 0, aprobado: 1, bloqueado: 2 };
    us.sort((a, b) => (orden[a.estado] - orden[b.estado]) || String(a.nombre).localeCompare(String(b.nombre)));
    this.pendientes = us.filter(u => u.estado === "pendiente").length; this.pintarAviso();
    l.innerHTML = "";
    for (const u of us) {
      const d = document.createElement("div"); d.className = "fila-u";
      d.innerHTML = '<div class="n"></div><div class="c"></div><div class="e"></div><div class="b"></div>';
      d.querySelector(".n").textContent = u.nombre || "(sin nombre)";
      d.querySelector(".c").textContent = u.email || "";
      const e = d.querySelector(".e"); e.className = "e " + u.estado;
      e.textContent = { pendiente: "Pendiente de aprobar", aprobado: "Aprobado", bloqueado: "Bloqueado" }[u.estado] || u.estado;
      const b = d.querySelector(".b");
      const boton = (txt, estadoNuevo, cls) => {
        const x = document.createElement("button"); x.textContent = txt; if (cls) x.className = cls;
        x.onclick = async () => { x.disabled = true; try { await this.api.cambiarEstado(u.uid, estadoNuevo); } catch (_) { alert("No se pudo cambiar."); } this.pintarAdmin(); };
        b.appendChild(x);
      };
      if (u.uid === this.uid) { b.remove(); e.textContent += " (tú)"; }
      else if (u.estado === "pendiente") { boton("Aprobar", "aprobado", "si"); boton("Rechazar", "bloqueado"); }
      else if (u.estado === "aprobado") boton("Bloquear", "bloqueado");
      else boton("Aprobar", "aprobado", "si");
      l.appendChild(d);
    }
    if (!us.length) l.innerHTML = '<p class="ayuda">Todavía no hay usuarios.</p>';
  },
};
