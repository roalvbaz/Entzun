# Activar las cuentas (Firebase, plan gratis)

Hasta que hagas esto, Entzun funciona con perfiles locales (sin contraseña). Cuando pegues tu configuración en `firebase-config.js`, la app pasa a pedir **cuenta y contraseña**, con **aprobación del administrador** y progreso sincronizado entre móviles.

No hace falta tarjeta de crédito: Auth y Firestore entran en el plan gratuito (Spark).

## 1. Crear el proyecto
1. Abre https://console.firebase.google.com e inicia sesión con tu cuenta de Google.
2. **Crear un proyecto** → nombre `entzun` → desactiva Google Analytics → **Crear**.

## 2. Activar el inicio de sesión
1. Menú **Compilación → Authentication → Comenzar**.
2. Pestaña **Método de acceso** → activa **Correo electrónico/contraseña** (solo la primera casilla) y guarda.
3. Añade **Google** → actívalo, elige tu correo como correo de asistencia y guarda.
4. Pestaña **Configuración → Dominios autorizados → Añadir dominio**: `roalvbaz.github.io`.

## 3. Crear la base de datos
1. **Compilación → Firestore Database → Crear base de datos**.
2. Ubicación: `eur3 (europe)` (o la más cercana). Modo: **producción**.
3. Pestaña **Reglas**: borra lo que haya, pega el contenido de `firestore.rules` de este repositorio y pulsa **Publicar**.

## 4. Copiar la configuración de la web
1. Engranaje ⚙ → **Configuración del proyecto** → **Tus apps** → icono web `</>` → nombre `entzun` → **Registrar app** (sin Hosting).
2. Copia el bloque `firebaseConfig` (apiKey, authDomain, projectId, appId...).
   Estos valores **no son secretos**; los puedes pegar en el chat o en `firebase-config.js`:

```js
export const FIREBASE_CONFIG = {
  apiKey: "...",
  authDomain: "....firebaseapp.com",
  projectId: "...",
  appId: "..."
};
```

## 5. Hacerte administrador (una sola vez)
1. Abre la app y pulsa **Crear cuenta** con tu correo. Verás «Cuenta pendiente».
2. En Firebase: **Authentication → Usuarios** y copia tu **UID de usuario**.
3. **Firestore Database → Datos → Iniciar colección** → ID de colección `admins` → ID de documento = tu UID → campo `activo` (boolean) = `true` → Guardar.
4. Vuelve a la app y pulsa **Comprobar otra vez**: entras como administrador y tu cuenta se aprueba sola.

## 6. Añadir a los demás
Cada persona pulsa **Crear cuenta** (con correo o con Google). Aparece como *pendiente*; tú la ves en el inicio («1 persona espera tu aprobación») y la apruebas o rechazas desde **tu círculo → Gestionar usuarios**.

## Notas
- Los MP3 siguen en el repositorio público de GitHub: la app exige cuenta, pero un archivo de audio con su dirección exacta se puede abrir. Proteger los audios de verdad requiere almacenamiento de pago.
- «Entrar con Google» en la app instalada en la pantalla de inicio del iPhone puede fallar por limitaciones de iOS; con correo y contraseña siempre funciona.
- Para quitar a alguien: **Bloquear** en el panel (no puede entrar ni guardar progreso).
- Sin conexión, quien ya había entrado sigue pudiendo usar la app con su progreso local.
