# OneToEight Agent: panorama y flujo de configuración

El **OneToEight Agent** es un asistente de IA personalizado
construido sobre
[Hermes Agent](https://hermes-agent.nousresearch.com/docs) para
jóvenes que aprenden a poner los **Ocho Esenciales** en la práctica
diaria. Es un mentor amable que ejecuta un ritmo diario de planes
de audio, check-ins de reflexión y pequeñas acciones, enseñado
desde la guía de los Ocho Esenciales que viene con el repo.

Este README es el panorama y el flujo para poner el agente en
marcha de principio a fin. Léelo una vez y luego recorre los pasos.

> **Dos formas de empezar.** Recorre el **build path** y construye
> el agente pieza por pieza: una capacidad, un beneficio, cada
> semana, con audio para seguir. O instálalo con el flujo de
> configuración de abajo.
>
> **Empieza el build path: <https://gladtobe.here.now/build-path/>**

> Léelo en: **Español** · [English](README.md) · [Bahasa Melayu](README.ms.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Filipino](README.tl.md) · [中文](README.zh.md) · [한국어](README.ko.md) · [日本語](README.ja.md)

---

## Qué es este producto

Un joven aprende los Ocho Esenciales mejor **haciendo una cosa
pequeña cada día** durante semanas y meses, no leyendo un libro.
El OneToEight Agent existe para que ese ritmo diario se sostenga:

- Un **Minuto de la Mañana** llega a la hora elegida en el chat
  del joven (Telegram o WhatsApp). Es un plan breve de audio para
  el día, más texto.
- Un **Check-in de la Tarde** llega por la tarde. Es un mensaje de
  texto corto: cómo fue el día, qué sigue, una pregunta para
  pensar durante la noche.
- Una **Sesión de Planificación** llega antes de dormir. Traza el
  día siguiente: tareas de la escuela, fechas de entrega, el
  esencial en el que está trabajando esta semana, una cosa real
  que quiere hacer. El agente redacta el plan, el joven lo edita
  y este se guarda en local: sin app, sin cuenta, sin
  sincronización en la nube.
- El agente enseña desde la **guía de los Ocho Esenciales**
  guardada en el repo (`essentials/01..08/lessons/*.md`),
  ramificando según la tradición que elija el joven.
- La guía también está publicada en **diez idiomas**: se puede
  leer en línea o descargar como paquete sin conexión para usarla
  sin internet. Ver `essentials/guide-editions.md`.

El agente no da sermones. Extrae la sabiduría del joven con
preguntas, sostiene el ritmo con suavidad y lo ayuda a retomarlo
cuando se cae, sin regañarlo.

### Dos tradiciones, o la tuya propia

Cada joven elige una en el onboarding. O dile al agente tu
tradición y la incorporará. El agente se mantiene dentro de la
tradición elegida; nunca mezcla tradiciones:

- **Cristiana**: anclada en la Biblia. El Minuto de la Mañana
  incluye cada mañana un versículo bíblico, leído con naturalidad.
  El check-in enmarca el día dentro de una fe viva.
- **Universal (secular)**: tradiciones de sabiduría respetadas
  sin doctrina. El Minuto de la Mañana incluye una breve reflexión
  o una pregunta de un pensador. El check-in enmarca el día dentro
  de la reflexión, la gratitud y la intención.

El joven puede cambiar de tradición más adelante, pero las
lecciones se ramifican desde ese momento.

### Dos órdenes de entrega

Cada joven también elige cómo se sirven los Ocho Esenciales:

- **Secuencial** (predeterminado): recorre los esenciales 1 a 8 en
  orden. Es el más coherente y es el orden para el que se escribió
  la guía. Recomendado para jóvenes nuevos.
- **Aleatorio**: saca cualquier esencial cualquier día, ajustado a
  lo que el joven parece necesitar ese día (el intervalo más
  largo, la dificultad reciente, la energía del día). Cada Minuto
  de la Mañana abre con un resumen de conocimiento del esencial
  elegido, más una pequeña actividad. Ideal para jóvenes que ya
  saben lo que necesitan.

En ambos modos, **los ocho esenciales se cubren tarde o
temprano.** El joven puede cambiar más adelante actualizando la
clave de memoria `essentials_order`, sin tener que repetir el
onboarding.

### Los Ocho Esenciales (en el orden en que los enseña la guía)

1. **La capacidad de estar en silencio**: quedarte quieto, a solas con tus propios pensamientos
2. **Tu cuerpo es un hogar**: sueño, comida, agua, movimiento, luz del sol
3. **Habilidades útiles para la vida real**: cocinar, reparar, construir, manejar un presupuesto
4. **Autodefensa digital**: privacidad, atención, conocimiento de tu identidad
5. **Comunidad real**: personas que saben tu nombre
6. **Conocimiento sin Wi-Fi**: propio, no alquilado
7. **Recetar la naturaleza**: tiempo al aire libre prescrito, no negociable
8. **Convicciones probadas**: tuyas, y resisten bajo presión

---

## Cómo funciona

### El ciclo diario

```
06:00  Minuto de la Mañana       Audio de Piper + texto → Telegram o WhatsApp
       ↓
día    El joven hace la pequeña acción del día
       ↓
17:00  Check-in de la Tarde      Solo texto → Telegram o WhatsApp
       ↓
21:00  Sesión de Planificación   Solo texto → Telegram o WhatsApp
       El agente redacta el plan de mañana → el joven lo edita → se guarda en local
       ↓
       Dormir
       ↓
       Repetir
```

El agente refuerza el ciclo sin insistir. Los días perdidos se
retoman con suavidad. Sin regaños. Sin moralizar.

**Sobre el horario:** las horas de arriba están en la zona horaria
local del joven. El daemon de cron guarda los horarios en
**UTC**. Si eliges las 6 de la mañana en UTC+10, el cron guarda
`0 20 * * *` (20:00 UTC). El horario es siempre "la hora en tu
zona horaria": la conversión a UTC es automática.

### La tarea del agente en cada momento

| Cuándo | El agente |
|---|---|
| Primer chat en un perfil nuevo | Ofrece la orientación, brevemente, con su propia voz |
| El joven dice "configúrame" | Ejecuta `agent-onboarding` (con consentimiento, por fases) |
| El joven hace una pregunta | Lee los `essentials/<NN-name>/lessons/*.md` relevantes, sintetiza, enseña |
| Se dispara el cron del Minuto de la Mañana | Genera el plan del día, ejecuta Piper, sube el audio, lo entrega en el chat |
| Se dispara el cron del Check-in | Lee el Minuto de la Mañana más reciente, redacta una reflexión breve, la entrega como texto |
| Se dispara el cron de la Sesión de Planificación | Redacta el plan de mañana (tareas de la escuela, fechas de entrega, esencial de la semana, una cosa del mundo real), el joven lo edita, se guarda en local |
| El joven pide profundizar | Usa la skill `eight-essentials-curriculum`: lee la guía y enseña desde ella |

### Qué se ejecuta en segundo plano

Tres trabajos de cron, todos apagados hasta que el joven los
aprueba en el onboarding:

1. **Minuto de la Mañana**: se dispara a la hora elegida en la
   zona horaria del joven, todos los días (o solo días de semana,
   si se prefiere). Genera audio + texto y lo entrega a Telegram
   o WhatsApp.
2. **Check-in de la Tarde**: se dispara a la hora elegida de la
   tarde, con la misma regla de días que el Minuto de la Mañana.
   Envía un mensaje de texto corto.
3. **Sesión de Planificación**: se dispara antes de dormir
   (predeterminado 9 pm), con la misma regla de días. Redacta el
   plan de mañana para que el joven lo edite y luego lo guarda en
   local.

Los tres son **opt-in**: la orientación los crea solo después de
una aprobación explícita.

### Las veinte preguntas diarias

Una pequeña biblioteca de preguntas de cabecera que un joven
puede hacerle al OneToEight Agent en cualquier momento. El agente
lee el capítulo correspondiente de la guía, se apoya en lo que ya
sabe del joven y responde con su voz, en su tradición.

El punto **no** es responder las veinte cada día. El punto es
tener un conjunto pequeño de preguntas de cabecera que saquen a
la superficie los esenciales, provoquen reflexión y conviertan la
curiosidad en una práctica diaria. Elige una o dos. Salta el
resto. Rota a lo largo de la semana.

Las preguntas están escritas en la voz del joven. El agente no
responde con sermones. Hace la pregunta, da espacio para la
respuesta y sigue con una pequeña acción.

El archivo completo de preguntas está en
`essentials/00-introduction/lessons/prompts.md`. El agente lo lee
cuando el joven pide "algo para pensar", una pregunta con la
que quedarse o ayuda cuando está atascado.

#### Por modo

| Modo | Preguntas |
|---|---|
| Autorreflexión | #1, #3, #6, #7, #12, #15, #16, #20 |
| Actividad | #2, #9, #13, #14, #17, #19 |
| Pensamiento crítico | #5, #8, #10, #18 |
| Ritual diario | #11, #16, #20 |

#### Por energía

| Energía | Preguntas sugeridas |
|---|---|
| Cansado, bajo | #1, #20, #11 |
| Acelerado, curioso | #5, #10, #14 |
| Atascado o plano | #3, #9, #15 |
| Con ganas de pensar | #4, #6, #16, #18 |
| Con ganas de hacer | #2, #9, #13, #17, #19 |

#### Por esencial (cada esencial aparece al menos dos veces)

| Esencial | Preguntas que se inclinan hacia él |
|---|---|
| Silencio | #1, #7, #9, #12, #16 |
| El cuerpo | #2, #9, #14, #19 |
| Habilidades útiles | #8, #13, #14 |
| Autodefensa digital | #4, #8, #18 |
| Comunidad real | #6, #15, #17 |
| Conocimiento sin Wi-Fi | #3, #6, #8, #10, #11 |
| Naturaleza | #9, #19 |
| Convicciones probadas | #1, #5, #7, #10, #16, #18 |

#### Preguntas pesadas (úsalas poco)

Las preguntas **#1**, **#5**, **#10** y **#18** son pesadas. El
agente nunca se apoya en ellas. El joven tiene que pedirlas por
su nombre. Si el joven pide una pregunta pesada y el agente
juzga que es el día equivocado, puede ofrecer con suavidad una
alternativa más ligera y explicar por qué.

#### Las veinte

| # | Pregunta | Modo | Energía | Esenciales |
|---|----------|------|--------|------------|
| 1 | Pregúntame algo que probablemente no quiero responder, pero debería. | Autorreflexión | Cansado / bajo | Los ocho (esp. Convicciones probadas, Silencio) |
| 2 | Dame una tarea de 10 minutos que me incomode de una forma útil. | Actividad | Con ganas de hacer | El cuerpo, Silencio, Convicciones probadas |
| 3 | ¿Qué hice hace tres días que no he vuelto a hacer desde entonces? ¿Por qué? | Autorreflexión | Atascado / plano | Conocimiento de ti mismo, Conocimiento sin Wi-Fi |
| 4 | Elige un esencial en el que soy más débil. ¿Cuál es la práctica más pequeña que podría hacer hoy? | Pensamiento crítico | Con ganas de pensar | Los ocho (diagnóstico) |
| 5 | Discute en contra de mi última decisión. ¿Qué diría un crítico sabio? | Pensamiento crítico | Acelerado / curioso | Conocimiento sin Wi-Fi, Convicciones probadas |
| 6 | Si tuviera que enseñarle a un joven que empieza la secundaria una cosa que aprendí este año, ¿cuál debería ser? | Autorreflexión | Con ganas de pensar | Conocimiento sin Wi-Fi, Comunidad real |
| 7 | ¿En qué parte de mi vida estoy actuando en vez de hacer de verdad? ¿Dónde estoy haciendo de verdad en vez de actuar? | Autorreflexión | Cansado / bajo | Convicciones probadas, Silencio |
| 8 | ¿Qué estoy dejando en manos de otros que debería estar construyendo yo mismo? | Pensamiento crítico | Con ganas de pensar | Habilidades útiles, Autodefensa digital, Conocimiento sin Wi-Fi |
| 9 | Dame una actividad de 30 minutos que no requiera teléfono ni a nadie más. | Actividad | Atascado / plano | El cuerpo, Silencio, Naturaleza |
| 10 | ¿Qué creencia sostengo que no podría defender si me presionan? ¿Debería conservarla de todos modos? | Pensamiento crítico | Acelerado / curioso | Convicciones probadas, Conocimiento sin Wi-Fi |
| 11 | Hazme una prueba de algo que olvidé que sabía. | Ritual diario | Cansado / bajo | Conocimiento sin Wi-Fi |
| 12 | Pregúntame por la última vez que estuve genuinamente aburrido y qué noté en el silencio. | Autorreflexión | Atascado / plano | Silencio, El cuerpo |
| 13 | Sugiéreme una cosa que podría terminar hoy y que empecé hace más de una semana. | Actividad | Con ganas de hacer | Habilidades útiles, Convicciones probadas |
| 14 | Guíame por algo práctico que todavía no sé hacer: alimentarme, arreglar un pinchazo, escribir un CV, cambiar una rueda. | Actividad | Acelerado / curioso | Habilidades útiles, El cuerpo |
| 15 | ¿Quién en mi vida aparecería a las 2 de la mañana? ¿Quién no? ¿Por qué? | Autorreflexión | Atascado / plano | Comunidad real |
| 16 | Compara cómo pasé mi tiempo hoy con cómo dije que quería pasarlo. ¿Dónde está la diferencia? | Ritual diario | Con ganas de pensar | Convicciones probadas, Silencio |
| 17 | Dame un tema para iniciar una conversación que pueda usar con alguien con quien no he hablado bien en un tiempo. | Actividad | Con ganas de hacer | Comunidad real |
| 18 | Si borrara todas las apps de mi teléfono excepto tres, ¿cuáles deberían quedarse y por qué? | Pensamiento crítico | Con ganas de pensar | Autodefensa digital, Convicciones probadas |
| 19 | Sácame a caminar 15 minutos. ¿Qué debería mirar, escuchar y notar de verdad? | Actividad | Con ganas de hacer | Naturaleza, El cuerpo, Silencio |
| 20 | Termina el día conmigo. Tres cosas que pasaron, tres que noté, una por la que estoy agradecido. | Ritual diario | Cansado / bajo | Los ocho (cierre del día) |

#### Cómo las usa el agente

El agente lee
`essentials/00-introduction/lessons/prompts.md` cada vez que el
joven pide una pregunta. **No** le pega preguntas al joven.
Menciona una, invita al joven a leerla y da espacio para la
respuesta. Nunca hace tres preguntas seguidas.

En el orden de entrega **secuencial**, las preguntas se agrupan
de forma natural alrededor del esencial en el que está el joven.
En el orden **aleatorio**, el agente elige la pregunta que
encaja con el momento. Los ocho esenciales siguen disponibles en
ambos modos.

---

## Los rituales diarios

Este es el mapa de un vistazo de todos los rituales que ejecuta el
agente: qué son, cuándo se disparan, dónde llegan y dónde están
documentados en detalle.

| Ritual | Cuándo | Canal | Qué pasa |
|---|---|---|---|
| **Minuto de la Mañana** | Cada día a la hora elegida por el joven (predeterminado 6 am) | Telegram o WhatsApp, **nota de voz + texto** | Plan de audio para el día, centrado en una pequeña acción del esencial actual. |
| **Check-in de la Tarde** | Cada día a la hora elegida por el joven (predeterminado 5 pm) | Telegram o WhatsApp, **solo texto** | Reflexión sobre cómo fue el día, plan para mañana, una pregunta para pensar durante la noche. |
| **Sesión de Planificación** | Cada día antes de dormir a la hora elegida por el joven (predeterminado 9 pm) | Telegram o WhatsApp, **solo texto** | El agente redacta el plan de mañana (tareas de la escuela, fechas de entrega, el esencial de la semana, una cosa del mundo real). El joven lo edita. Se guarda en local. |
| **Resumen del Esencial** | A pedido, cuando el joven lo pida | Telegram o WhatsApp, **nota de voz** | Resumen hablado de 3 a 5 minutos de un esencial, más una breve lista escrita de puntos clave. |
| **Lección del Esencial** | A pedido, cuando el joven lo pida | here.now, **enlace a una página HTML en el chat** | Lección de tres páginas sobre un esencial, con fuentes citadas, citas clave y un quiz corto. |
| **Poema del Esencial** | A pedido, cuando el joven lo pida | Telegram o WhatsApp, **nota de voz + texto** | Un poema rimado recitado sobre el esencial, leído en voz alta con el texto debajo. |
| **Canción del Esencial** | A pedido, cuando el joven lo pida | Telegram o WhatsApp, **nota de voz MP3 + texto** | El agente escribe un poema sobre el esencial y luego lo convierte en una canción real con Google Lyria 3 en OpenRouter. Cuesta ~$0.08 por canción; confirma antes de ejecutar. |
| **Video Musical del Esencial** | A pedido, cuando el joven lo pida | here.now, **enlace a un video MP4 en el chat** | La canción de arriba, más un storyboard de imágenes fijas unidas al audio y una superposición opcional del texto del poema. Cuesta ~$0.35 en total; confirma antes de ejecutar. |

**El día.** El Minuto de la Mañana abre el día, el Check-in lo
cierra y la Sesión de Planificación traza el mañana antes de
dormir. Los tres formatos a pedido (Resumen / Lección / Poema)
están ahí siempre que un joven quiera aprender un esencial con
más profundidad de la que el Minuto de la Mañana puede cubrir en
un minuto.

**Dónde vive el código.** Cada fila enlaza con una skill del repo:

| Ritual | Ruta de la skill |
|---|---|
| Minuto de la Mañana | `skills/hermes/morning-minute/` |
| Check-in de la Tarde | `skills/profile/afternoon-checkin/` |
| Sesión de Planificación | `skills/profile/planning-session/` |
| Resumen, Lección, Poema, Canción, Video Musical | `skills/profile/essential-deep-dives/` (Canción y Video Musical usan `skills/creative/openrouter-lyria-music/` y `skills/creative/poem-song-video-studio/`) |

**Consentimiento.** Los tres rituales basados en cron (Minuto de
la Mañana, Check-in, Sesión de Planificación) están apagados hasta
que el joven o el padre o la madre los aprueba durante el
onboarding. Los cinco formatos a pedido (Resumen, Lección, Poema,
Canción, Video Musical) están disponibles de inmediato: basta con
que el joven los pida. Los dos formatos pagos (Canción y Video
Musical, Lyria 3 + imágenes del storyboard) requieren que el joven
confirme el gasto cada vez que le pide uno al agente. Ver [El flujo
de configuración → Qué se ejecuta en segundo
plano](#qué-se-ejecuta-en-segundo-plano) para el flujo exacto de
opt-in.

**Skills de Canción y Video Musical.** Los dos formatos pagos
reutilizan dos skills existentes en vez de reinventarlas:

| Formato | Skill subyacente | Qué agrega sobre `essential-deep-dives` |
|---|---|---|
| **Canción del Esencial** | `skills/creative/openrouter-lyria-music/` | Letra del POEMA → audio MP3 con Google Lyria 3 (~$0.08/canción). |
| **Video Musical del Esencial** | `skills/creative/poem-song-video-studio/` | CANCIÓN + ~8 imágenes de storyboard + ffmpeg → MP4 (~$0.35 en total). |

Ambas skills ya existen en el repo con notas completas del modelo
Lyria 3, scripts y un control de gastos. El agente carga la skill
subyacente cuando el joven pide el formato.

**Cómo personalizar.** El agente guía al joven para elegir la
hora, la zona horaria y la regla de días de cada ritual de cron
durante la configuración. Los tres se pueden pausar, reanudar o
eliminar más adelante con `cronjob(action="...")`. Los formatos a
pedido eligen la tradición del joven automáticamente; su voz y su
duración se heredan de la voz Piper ya elegida para el Minuto de
la Mañana.

---

## Cuánto cuesta ejecutarlo

El OneToEight Agent funciona **pago por uso**: sin suscripción.
Recargas una cuenta de OpenRouter y el agente consume de ese
crédito.

| Gasto | Monto | Notas |
|---|---|---|
| **Primer mes** | **unos $20** | Cubre la configuración más el primer mes de uso real mientras el joven se adapta |
| **Continuo** | **$5–$10 al mes** | Uso diario ligero con modelos de bajo costo |

El perfil se apoya en modelos de bajo costo para el trabajo
rutinario:

- **DeepSeek V4 Flash**: el predeterminado para el chat diario y
  las lecciones.
- **Google Gemini 3.7 Flash**: el respaldo rápido para tareas
  cortas.
- **Modelos de código abierto** (niveles gratis o casi gratis):
  para trabajo básico y de alto volumen que no necesita un modelo
  de frontera.

Los niveles gratuitos rotan mes a mes, así que la lista exacta
cambia. Ver la lista en vivo de modelos gratuitos en
<https://openrouter.ai/openrouter/free>. El perfil usa por defecto
opciones baratas y solo recurre a un modelo más grande cuando una
tarea realmente lo necesita.

---

## Tutoriales

¿Prefieres una guía paso a paso? El centro de tutoriales reúne
todas las páginas de configuración en un solo lugar:

- **El build path**: siete páginas que enseñan construyéndolo: el agente, armado pieza por pieza, con audio para seguir. Empieza en <https://gladtobe.here.now/build-path/>.
- **El currículo de onboarding**: siete páginas: el curso de instalación, desde la primera instalación hasta un agente conectado al chat.
- **Las hojas de recorrido**: la configuración en una sola página, en tres idiomas.

Abre el centro en <https://gladtobe.here.now/hub-tutorials.html>.
El flujo de abajo cubre el mismo terreno en texto, paso a paso.

---

## El flujo de configuración

### 1: Requisitos previos (una sola vez, en la máquina)

Necesitas:

- **Hermes Agent** instalado. Verificación rápida: `hermes --version`. Ver la [guía de instalación](https://hermes-agent.nousresearch.com/docs).
- **Python 3.10 a 3.13** (no el shim de la Windows Store; una instalación real). `python --version`.
- **Piper TTS.** Una instalación que funcione. Ver el Paso 2 abajo.
- **ffmpeg** para la conversión WAV → OGG. `ffmpeg -version`.
- **Una clave de proveedor de modelos.** El perfil usa por defecto `openrouter + deepseek-v4-flash`. Una sola clave abre un catálogo enorme de modelos, incluidos los de nivel gratuito y los multimodales (imagen, audio). Regístrate gratis en <https://openrouter.ai/> y agrega la clave con `hermes setup`. OpenCode Go es el respaldo.
- **Una clave API gratuita de Jina AI** para la búsqueda web. Regístrate gratis en <https://jina.ai/>: sin tarjeta de crédito. El nivel gratuito alcanza para el uso diario de un joven.
- **Un bot de Telegram** (recomendado) o un puente de WhatsApp. Telegram es mucho más fácil; ver el Paso 4.

### 2: Descomprime el perfil (una sola vez)

Tienes el perfil como un archivo zip, `onetoeight-agent-es.zip`.
Descomprímelo dentro de `~/.hermes/profiles/` para que quede como
`~/.hermes/profiles/onetoeight-agent/`, y luego:

```bash
mkdir -p ~/.hermes/profiles
# descomprime onetoeight-agent-es.zip dentro de esta carpeta
hermes profile use onetoeight-agent
hermes chat
```

> **Nota:** el directorio del perfil se llama `onetoeight-agent`,
> no `onetoeight`. Actualiza en consecuencia los comandos que
> hacen referencia a la ruta del perfil.

Para actualizar más adelante: descarga el nuevo zip y
descomprímelo en una carpeta temporal. Copia los archivos nuevos
encima, pero **no borres** tu carpeta `memories/` ni tus sesiones
guardadas. El `LOCALE.md` en la raíz de la carpeta registra de qué
versión se compiló esto.

### 3: Primer chat → orientación

En el primer chat, el agente abre con:

> "Antes de entrar de lleno: ¿quieres que te guíe por la
> configuración? Toma un par de minutos y deja tus herramientas,
> tu memoria y el Minuto de la Mañana funcionando como tú quieres.
> O podemos saltarlo y empezar directamente."

Di que sí (o simplemente pide *"ayúdame a configurar mi perfil"*
en cualquier momento). Se ejecuta la skill `agent-onboarding`.

### 4: La orientación (con control de consentimiento)

La orientación es conversacional. El agente hace un grupo pequeño
de preguntas relacionadas por vez y **se detiene en cada paso de
credenciales**: nunca pide claves ni tokens en el chat.

Esto es lo que cubre, en orden:

| Paso | Qué pasa | Dónde agregas las cosas |
|---|---|---|
| 1. Identidad | Nombres (el tuyo, el del joven, el del agente), estilo de respuesta y el idioma para la guía, las lecciones y los mensajes | Guardado en la memoria del perfil |
| 2. Perfil y vida | Edad, ubicación, situación de vivienda, forma de la semana, 3 intereses, objetivo de enfoque, círculo de amistades, bloqueo, temas fuera de límites: los campos que el agente usa para adaptar el Minuto de la Mañana y las lecciones | Guardado en la memoria del perfil |
| 3. Tradición | Cristiana, Universal, o la suya propia | Guardado en la memoria del perfil |
| 4. Instalación de Piper + voz | Verifica que Piper funcione, elige una voz, descarga el modelo de voz | Modelo de voz en `piper-voices/` |
| 5. Clave API de Jina | Regístrate gratis, agrégala a `.env`, el agente verifica con una búsqueda real | `JINA_API_KEY=` en `.env` |
| 6. Canal de entrega | Credenciales del bot de Telegram o WhatsApp | `TELEGRAM_BOT_TOKEN=` / `WHATSAPP_*` en `.env` |
| 7. Guía de los Ocho Esenciales | Confirma que los archivos MD de las lecciones estén en `essentials/01..08/lessons/`, y comparte la edición de la guía en el idioma del joven (`essentials/guide-editions.md`) | Archivos en el repo |
| 8. Memoria | Se recomienda Mnemosyne (local, sin cuenta externa) | `hermes memory setup` |
| 9. Horario del Minuto de la Mañana | Qué hora, qué zona horaria, qué días | Se crea como trabajo de cron |
| 10. Horario del Check-in de la Tarde | Qué hora, qué zona horaria, qué días | Se crea como trabajo de cron |
| 11. Horario de la Sesión de Planificación | Qué hora (predeterminado 9 pm), qué zona horaria, qué días | Se crea como trabajo de cron |
| 12. Token Router (opcional) | El plugin que reduce la superficie de herramientas | `plugins.enabled` en `config.yaml` |

Al final, el agente muestra un resumen de la **configuración
propuesta** y espera tu aprobación explícita antes de aplicar
nada.

### 5: Verifica cada componente

Antes del primer Minuto de la Mañana programado, verifica cada
componente:

```bash
# Piper works — test synthesis (paths vary by OS; see below)
echo "The Morning Minute is ready." | piper -m piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx -f /tmp/piper-test.wav

# Jina works
curl -s -H "Authorization: Bearer ***" \
  "https://s.jina.ai/https://hermes-agent.nousresearch.com/docs"
# → clean snippet of the docs page means it works

# Telegram bot works (sends a test message)
# Use the test script in Step 3 of the Telegram setup below.
# If you get "chat not found", you must first send any message to your bot in Telegram.

# Guide MD files are present
for d in essentials/*/lessons/; do echo "--- $d ---"; ls "$d"; done

# Mnemosyne is configured
hermes memory status

# Cron jobs are queued
cronjob(action="list")
```

**Ubicaciones del binario de Piper por plataforma:**

| Plataforma | Ruta típica |
|---|---|
| Linux | `/data/.hermes/bin/piper/piper` |
| macOS (Homebrew) | `/opt/homebrew/bin/piper` |
| macOS (manual) | `~/Library/Piper/piper` |
| Windows | `C:/Users/<you>/.openhuman/bin/piper/piper/piper.exe` |
| Windows (pip) | `pip install piper-tts`, luego `piper` en el PATH |

La orientación busca Piper y lo encuentra si está en tu PATH. Si
está instalado en un lugar poco habitual, la orientación te
pedirá la ruta.

**Dónde se guardan los modelos de voz** (descárgalos una vez,
úsalos para siempre):

| Voz | Región | Ruta en Hugging Face |
|---|---|---|
| `en_US-joe-medium` | EE. UU., hombre | `rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx` |
| `en_US-amy-medium` | EE. UU., mujer | `rhasspy/piper-voices/resolve/main/en/en_US/amy/medium/en_US-amy-medium.onnx` |
| `en_GB-alan-medium` | Reino Unido, hombre | `rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx` |
| `en_GB-jenny_dioco-medium` | Reino Unido, mujer | `rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx` |
| `en_AU-natasha-medium` | Australia, mujer | `rhasspy/piper-voices/resolve/main/en/en_AU/natasha/medium/en_AU-natasha-medium.onnx` |

Patrón de descarga (ejemplo, Joe en Linux):

```bash
mkdir -p ~/.hermes/piper-voices/en/en_US/joe/medium
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -sL --fail \
  "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json" \
  -o ~/.hermes/piper-voices/en/en_US/joe/medium/en_US-joe-medium.onnx.json
```

### 6: La primera ejecución programada

El Minuto de la Mañana se dispara a la próxima hora programada en
la zona horaria del joven. Genera audio (Piper), lo sube a
here.now para obtener una URL pública y luego entrega ese audio
directamente a Telegram mediante una carga multipart, **no** con
un enlace `MEDIA:<url>` (la configuración de Cloudflare de
here.now bloquea al bot de descarga de archivos de Telegram). El
Check-in se dispara a la próxima hora programada de la tarde.

### 7: Operación del día a día

El joven no interactúa con el agente a través de una terminal
todos los días. El chat de Telegram o WhatsApp **es** la
superficie diaria:

- El **Minuto de la Mañana** llega como nota de voz + plan en texto.
- El **Check-in de la Tarde** llega como texto.
- La **Sesión de Planificación** llega antes de dormir como texto: el agente redacta el plan de mañana (tareas de la escuela, fechas de entrega, el esencial de la semana, una cosa del mundo real), el joven lo edita y este se guarda en local. Ver `skills/profile/planning-session/`.
- **Responde al check-in** con una nota de una línea sobre cómo fue el día. El agente guarda un resumen y lo usa como referencia en el Minuto de la Mañana del día siguiente.
- **Haz preguntas en cualquier momento.** "¿Cómo se ven en la práctica unas convicciones probadas?" "¿Cómo encuentro una comunidad real?" El agente lee la guía y enseña.

#### Formas más profundas de aprender un esencial (a pedido)

Más allá del ritmo diario, el joven puede pedir cualquiera de
los formatos más profundos sobre cualquier esencial. Todos los
maneja la skill `essential-deep-dives` (ver
`skills/profile/essential-deep-dives/`), y todos requieren solo
que los pida:

- **Resumen del Esencial**: los puntos clave de un esencial en
  lenguaje sencillo, más una **nota de voz** de 3 a 5 minutos que
  el agente genera (Piper) y deja en el chat para que el joven
  escuche mientras camina o hace tareas.
- **Lección del Esencial**: una hermosa **lección de tres
  páginas** construida como página HTML y publicada en la cuenta
  de **here.now** de la casa. Enseña el esencial con **fuentes
  citadas** (investigadas con la API de Jina cuando la lección
  necesita material que la guía no trae), **citas clave** y un
  **quiz** corto que el joven responde en la página. El agente
  envía el enlace en el chat.
- **Poema del Esencial**: un **poema recitado con rima** sobre el
  esencial, leído como nota de voz con el texto debajo para que
  el joven pueda seguir la lectura.
- **Canción del Esencial**: el agente escribe un poema original
  sobre el esencial y luego lo convierte en una canción real
  (MP3) con `google/lyria-3-pro-preview` en OpenRouter (~$0.08
  por canción). La nota de voz suena en el chat y el texto del
  poema va debajo. Confirma el gasto antes de ejecutar.
- **Video Musical del Esencial**: la Canción de arriba, más un
  storyboard de imágenes fijas unidas con el audio y una
  superposición opcional del texto del poema (~$0.35 en total por
  la canción + las imágenes del storyboard + el montaje con
  ffmpeg). Se publica como MP4 en here.now; el enlace va al chat.
  Confirma el gasto antes de ejecutar.

El agente lee la guía antes de redactar cualquiera de ellos, se
ramifica según la tradición del joven y se adapta a su perfil:
las mismas reglas que la skill del currículo.

### 8: Mantenimiento

De vez en cuando:

- `hermes update`: trae la biblioteca estándar de skills de Hermes
  al perfil (las skills curadas nunca se sobrescriben).
- `git -C ~/.hermes/profiles/onetoeight-agent pull`: obtiene
  mejoras del upstream para la guía o las skills.
- `cronjob(action="list")`: confirma que ambos trabajos siguen
  programados.

---

## Qué configurarás en `.env`

El perfil viene con `.env.example`, que muestra cada variable.
Aquí está lo que realmente configuras.

### Obligatorio (en cualquier configuración)

```bash
# Model provider key
OPENAI_API_KEY=...          # or your provider's key name

# Web search (free)
JINA_API_KEY=jina_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Obligatorio para la entrega por Telegram

```bash
# Get these from @BotFather in Telegram
TELEGRAM_BOT_TOKEN=1234567890:ABCDefghijklmnopqrstuvwxyz
TELEGRAM_CHAT_ID=123456789
```

> **Nota sobre la configuración de Telegram:** después de crear tu
> bot con @BotFather, **debes enviarle al menos un mensaje**
> (por ejemplo `/start`) antes de que el agente pueda enviarte
> cosas. Un bot que nunca ha recibido un mensaje fallará en
> silencio al intentar enviar.

Para encontrar tu chat ID: envíale un mensaje a `@userinfobot` en
Telegram y te responderá con tu ID numérico.

### Obligatorio para el audio (Minuto de la Mañana)

```bash
# here.now is a site publisher, not a drive. The API key is all you need.
# DRIVE_ID is not used by the audio publish flow — ignore it if you see it.
HERENOW_API_KEY=hn_xxxxxxx
```

> **Nota sobre here.now:** el audio se sube con la API de
> publicación de here.now, que devuelve una URL pública. Esa URL
> se envía a Telegram mediante una carga multipart, así que **no**
> necesita un DRIVE_ID. Si ves `HERENOW_DRIVE_ID` en documentos o
> ejemplos antiguos, es un remanente y el flujo actual de entrega
> de audio no lo usa.

### Integraciones opcionales

```bash
# Notion
NOTION_API_KEY=...

# GitHub (for tracking, opening issues)
GITHUB_TOKEN=...

# Bluesky (if you publish there)
BLUESKY_HANDLE=...
BLUESKY_APP_PASSWORD=...
```

### Cosas que NO son variables de entorno

- **Rutas de los modelos de voz**: se guardan en la memoria del
  perfil, no en env. La ruta depende de cada máquina.
- **Horarios de cron**: se configuran con
  `cronjob(action="create", ...)`, se guardan en el registro de
  cron, no en env.
- **Ruta del binario de Piper**: se guarda en la memoria del
  perfil.
- **Mnemosyne**: local, sin clave.

---

## Qué hay en el repo

```
onetoeight-agent/
├── README.md                              ← este archivo
├── SOUL.md                                ← persona y voz operativa
├── AGENTS.md                              ← principios operativos
├── profile.yaml                           ← descriptor del perfil
├── config.yaml                            ← configuración de ejecución de Hermes
├── .env.example                           ← cada variable, con comentarios
├── .gitignore
├── LICENSE                                ← MIT
│
├── essentials/                            ← contenido fuente de los Ocho Esenciales
│   ├── 00-introduction/lessons/
│   │   ├── christian.md                   ← Introducción (edición cristiana)
│   │   └── universal.md                   ← Introducción (edición universal)
│   ├── 01-silence/
│   │   ├── SKILL.md                       ← notas de enseñanza del agente para este esencial
│   │   ├── lessons/
│   │   │   ├── README.md                 ← esquema de archivos
│   │   │   ├── christian.md               ← Capítulo 1 (edición cristiana)
│   │   │   └── universal.md               ← Capítulo 1 (edición universal)
│   │   └── activities/README.md
│   ├── 02-body/        (misma estructura)
│   ├── 03-skills/      (misma estructura)
│   ├── 04-digital-self-defence/
│   ├── 05-community/
│   ├── 06-knowledge/
│   ├── 07-nature/
│   ├── 08-faith/
│   │   ├── lessons/
│   │   │   ├── christian.md               ← Convicciones probadas + personalización cristiana
│   │   │   └── universal.md               ← Convicciones probadas + personalización secular
│   │   └── activities/README.md
│   ├── 09-conclusion/lessons/{christian,universal}.md
│   ├── 10-before-after/lessons/{christian,universal}.md
│   └── guide-editions.md                  ← la guía en línea en diez idiomas
│
├── skills/
│   ├── hermes/                            ← skills curadas de Hermes
│   │   ├── agent-onboarding/  ← la orientación
│   │   ├── morning-minute/                ← plan diario + audio
│   │   ├── hermes-mnemosyne/              ← proveedor de memoria
│   │   ├── mnemosyne-maintenance/
│   │   └── skill-auditor/
│   └── profile/                       ← skills propias del perfil
│       ├── afternoon-checkin/           ← reflexión de la tarde
│       ├── eight-essentials-curriculum/   ← enseña desde la guía
│       ├── essential-deep-dives/          ← formatos resumen, lección, poema
│       └── setup-walkthrough/            ← configuración de Piper, Jina y el canal
│
├── plugins/hermes-token-router/           ← plugin opcional para reducir herramientas
├── memories/                              ← semillas genéricas de práctica operativa
└── skins/onetoeight.yaml                 ← tema de color
```

> **Skills estándar de Hermes** (web, terminal, github, creative,
> etc.) las trae `hermes update` y no forman parte de este repo.
> Están en la biblioteca estándar, no aquí.

---

## Referencia de configuración

### Proveedor de modelos (`config.yaml`)

```yaml
model:
  default: deepseek-v4-flash
  provider: openrouter
fallback_providers:
  - provider: opencode
    model: deepseek-v4-flash
```

Cambia `provider` y `default` para cambiar de proveedor.
OpenRouter es el predeterminado porque una sola clave abre el
catálogo más amplio (modelos gratuitos, además de multimodales de
imagen y audio) sin cambiar de proveedor. La cadena de respaldo se
ejecuta solo cuando el principal no está disponible.

### Toolsets (`config.yaml`)

Cada toolset de la CLI está **activo por defecto**. La orientación
guía al joven para revisar cada uno. Para desactivarlos
manualmente:

```bash
hermes --profile onetoeight-agent tools
# Or start with a specific set:
hermes --profile onetoeight-agent chat --toolsets "web,terminal,file,memory"
```

El toolset `tts` debe permanecer activo para el Minuto de la
Mañana.

### Trabajos de cron

Créalos con la orientación. Para gestionarlos manualmente:

```python
# List
cronjob(action="list")

# Create Morning Minute (UTC schedule — 6am AEST = 20:00 UTC)
cronjob(
    action="create",
    schedule="0 20 * * *",
    name="Morning Minute",
    prompt="""You are running the student's Morning Minute.
    Use the morning-minute skill. The student's tradition is
    <christian/universal>. Generate the day's plan, run Piper TTS,
    upload to here.now, deliver via multipart upload to Telegram.
    Do not write memories. Deliver only the final voice + text.""",
    skills=["morning-minute"],
    deliver="telegram",
)

# Weekdays only Morning Minute (6am, Mon–Fri)
cronjob(
    action="create",
    schedule="0 20 * * 1-5",
    name="Morning Minute",
    ...
)

# Pause without deleting
cronjob(action="pause", job_id="<id>")

# Resume
cronjob(action="resume", job_id="<id>")

# Remove (requires approval — deletes the schedule permanently)
cronjob(action="remove", job_id="<id>")
```

Ver `skills/hermes/morning-minute/SKILL.md` para el contrato
completo del cron del Minuto de la Mañana.

> **Entrega del cron:** la sesión de TUI/CLI no tiene un canal de
> entrega en vivo. Si quieres que te avisen cuando se dispare un
> cron, configura `deliver="telegram"` (o `deliver="all"`) al
> crearlo. Si no, los resultados se guardan en local y se pueden
> ver con `cronjob(action="list")`.

---

## Problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Piper falla al cargar | Ruta del modelo de voz incorrecta, o no está descargado | Vuelve a ejecutar el paso de Piper de la orientación |
| El audio del Minuto de la Mañana está en silencio o cortado | El texto de entrada del TTS se truncó | Verifica que el archivo de texto esté completo antes de sintetizar |
| El envío por Telegram falla con "chat not found" | El bot nunca ha recibido un mensaje | Abre Telegram, busca tu bot y envíale `/start` |
| El audio de Telegram no se reproduce | Se usa `MEDIA:<url>` con una URL de here.now | Usa la carga multipart con `sendVoice` (la skill se encarga de esto) |
| El cron se dispara a la hora equivocada | Confusión con UTC | El cron guarda UTC. 6 am UTC+10 = `0 20 * * *`. 6 am UTC-5 = `0 11 * * *` |
| El horario dice diario pero solo se dispara entre semana | Formato de cron incorrecto | `0 6 * * *` = todos los días. `0 6 * * 1-5` = lun–vie |
| La búsqueda de Jina no devuelve nada | La clave no está en `.env` o es incorrecta | Prueba con `curl -H "Authorization: Bearer ***" "https://s.jina.ai/"` |
| El agente da contenido de la tradición equivocada | La tradición no está en la memoria | Vuelve a ejecutar el paso de tradición de la orientación |
| El archivo de lección no se lee | Falta el sufijo `.christian.md` o `.universal.md` | Revisa `ls essentials/<NN>/lessons/`; los archivos deben tener el sufijo correcto |

---

## El plugin Token Router (opcional)

El Token Router es un plugin opcional de Hermes que **reduce la
superficie de herramientas** que ve el agente, no el joven. Cuando
está activo, el agente ve menos herramientas por defecto, lo que
puede reducir el uso de tokens y mantener al agente enfocado en
el trabajo de los Ocho Esenciales.

**No** oculta funciones al joven. El joven puede preguntar lo que
quiera; el router solo afecta lo que el agente elige
automáticamente.

Actívalo si:
- Quieres mantener al agente enfocado en enseñar, no en código ni en análisis de datos.
- El uso de tokens es una preocupación.

Déjalo apagado si:
- El joven (o su familia) quiere tener disponible toda la superficie de herramientas.

Para activarlo: `hermes plugins enable hermes-token-router`
(después de `hermes profile use onetoeight-agent`).

---

## Licencia

MIT: ver `LICENSE`.

La personalidad del OneToEight Agent es un arquetipo original de
asistente escrito para este proyecto. El contenido de la guía de
los Ocho Esenciales viene de la *Eight Essentials* de onetoeight,
Universal Edition V.3.0.0, incluida con permiso para usarse
dentro de este perfil.
