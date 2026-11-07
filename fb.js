// Carga el SDK de Firebase (Auth + Firestore) y expone una API pequeña en window.FB_READY.
// Resuelve: null -> sin configurar (modo local) | "fallo" -> no se pudo cargar | objeto api -> listo.
import { FIREBASE_CONFIG } from "./firebase-config.js";

const V = "10.12.2", BASE = `https://www.gstatic.com/firebasejs/${V}/`;

async function main() {
  if (!FIREBASE_CONFIG || !FIREBASE_CONFIG.apiKey || String(FIREBASE_CONFIG.apiKey).startsWith("PEGA")) {
    window.__fbResolve(null);
    return;
  }
  try {
    const [{ initializeApp }, A, F] = await Promise.all([
      import(BASE + "firebase-app.js"), import(BASE + "firebase-auth.js"), import(BASE + "firebase-firestore.js")]);
    const app = initializeApp(FIREBASE_CONFIG), auth = A.getAuth(app), db = F.getFirestore(app);
    const api = {
      onAuth: cb => A.onAuthStateChanged(auth, u => cb(u ? { uid: u.uid, email: u.email, displayName: u.displayName } : null)),
      registrar: (e, p) => A.createUserWithEmailAndPassword(auth, e, p),
      entrar: (e, p) => A.signInWithEmailAndPassword(auth, e, p),
      google: async () => {
        const prov = new A.GoogleAuthProvider();
        try { await A.signInWithPopup(auth, prov); }
        catch (e) {
          if (e.code === "auth/popup-blocked" || e.code === "auth/operation-not-supported-in-this-environment") await A.signInWithRedirect(auth, prov);
          else throw e;
        }
      },
      salir: () => A.signOut(auth),
      recuperar: e => A.sendPasswordResetEmail(auth, e),
      perfil: async uid => { const s = await F.getDoc(F.doc(db, "users", uid)); return s.exists() ? s.data() : null; },
      crearPerfil: (u, nombre) => F.setDoc(F.doc(db, "users", u.uid), {
        nombre: nombre || u.displayName || (u.email || "").split("@")[0], email: u.email || "", estado: "pendiente", creado: F.serverTimestamp() }),
      esAdmin: async uid => { try { return (await F.getDoc(F.doc(db, "admins", uid))).exists(); } catch (e) { return false; } },
      listarUsuarios: async () => (await F.getDocs(F.collection(db, "users"))).docs.map(d => ({ uid: d.id, ...d.data() })),
      cambiarEstado: (uid, estado) => F.updateDoc(F.doc(db, "users", uid), { estado }),
      leerProgreso: async uid => { const s = await F.getDoc(F.doc(db, "progreso", uid)); return s.exists() ? s.data() : null; },
      guardarProgreso: (uid, estado) => F.setDoc(F.doc(db, "progreso", uid), { estado: JSON.stringify(estado), actualizado: Date.now() }),
    };
    window.__fbResolve(api);
  } catch (e) {
    console.error("Firebase no cargó", e);
    window.__fbResolve("fallo");
  }
}
main();
