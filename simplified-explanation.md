# Computación cuántica explicada como si tuvieras 8 años

*Una guía para entender de verdad el proyecto `quantum-circuits-implementation`,
sin matemáticas que asusten. Si al terminar puedes explicárselo a un
niño, puedes explicárselo en una entrevista.*

---

## 🪙 Capítulo 1: La moneda mágica (el qubit)

Tú conoces las monedas normales: cara o sello. Una computadora normal
usa **bits**, que son como monedas que ya cayeron: o es 0 o es 1.

Un **qubit** es una moneda que está **girando en el aire**. Mientras gira,
no es cara ni es sello: ¡es las dos cosas a la vez! A eso los físicos
le dicen **superposición**.

Cuando la moneda cae (eso se llama **medir**), ahí sí: o cara o sello.
Pero mientras giraba, era ambas.

> 🧒 *"Entonces un qubit es una moneda que no ha caído todavía."*
> ¡Exacto! Y una computadora cuántica trabaja con miles de monedas
> girando al mismo tiempo.

---

## 🧤 Capítulo 2: Los guantes mágicos (el entrelazamiento)

Imagina que tienes dos guantes mágicos. Te pones uno, y mandas el otro
a la otra punta del mundo. Te quitas el tuyo y ves que es el **derecho**.
En ese mismo instante, sin que nadie te diga nada, **ya sabes** que el
otro guante es el **izquierdo**.

Los guantes no "se avisaron" — simplemente nacieron conectados. Eso es
el **entrelazamiento**: dos qubits que se comportan como una sola cosa,
aunque estén separadísimos.

Lo loco: antes de mirar, ninguno de los dos guantes era derecho ni
izquierdo. Solo al mirar uno, el otro "decide" ser el contrario.

> 🧒 *"¿Y eso sirve para algo?"*
> ¡Para todo! Es el ingrediente secreto de la teleportación y de muchos
> algoritmos cuánticos. Sin guantes mágicos no hay fiesta.

**En el proyecto:** el script `01_bell_state.py` fabrica un par de
guantes mágicos. Lo corre 2048 veces y comprueba que **siempre** salen
`00` o `11` (los dos iguales), nunca `01` ni `10`. Si alguna vez saliera
un `01`, el programa gritaría "¡los guantes se rompieron!".

---

## 📦 Capítulo 3: La teleportación (mover sin mover)

¿Te acuerdas de los guantes? Ahora imagina que quieres mandarle tu
moneda girando a un amigo, pero no puedes llevarla tú.

El truco de la teleportación cuántica:

1. Tú y tu amigo comparten un par de guantes mágicos (uno cada uno).
2. Tú juntas tu moneda con tu guante y los miras a los dos.
3. Le mandas a tu amigo un mensajito normal (un WhatsApp, digamos) con
   lo que viste: dos numeritos, 0 o 1.
4. Tu amigo hace un ajustecito a **su** guante según tu mensaje…
5. ¡Y pum! Su guante ahora gira **exactamente igual** que giraba tu
   moneda original.

Tu moneda original se "gastó" en el proceso (las reglas cuánticas no
permiten copiarla), pero su *giro* viajó sin moverse físicamente.

> 🧒 *"¿Eso es como en Star Trek?"*
> Casi, pero mejor: esto es real y se ha hecho en laboratorios de
> verdad. Solo que por ahora teleportamos el *giro de la moneda*, no
> personas. 😄

**En el proyecto:** `02_quantum_teleportation.py` teleporta el estado
`|1⟩` y verifica que el qubit del receptor termina en `|1⟩` en las
1024 corridas. 100% de éxito.

---

## 🔍 Capítulo 4: El detective rapidísimo (algoritmo de Grover)

Juguemos a las escondidas con 4 cajas. En una hay un premio. Tú,
como detective normal, abres cajas una por una: en promedio necesitas
abrir 2 o 3 para encontrarlo.

El detective cuántico hace algo tramposo: abre **las 4 cajas a la vez**
(superposición), y luego usa un truco matemático que hace que la caja
con el premio "brille más" y las otras "se apaguen". Después de una
sola ronda, casi siempre señala la caja correcta.

Con 4 cajas no impresiona mucho. Pero con **un millón** de cajas, el
detective normal abre 500.000 en promedio… y el cuántico solo **1.000**.
Esa es la magia: no es un poquito más rápido, es *radicalmente* más
rápido.

> 🧒 *"¿Y para qué sirve en la vida real?"*
> Para buscar en bases de datos gigantes, y —esto le importa a los
> espías— para debilitar algunos códigos secretos. Por eso los expertos
> en seguridad (como tú 😉) lo estudian.

**En el proyecto:** `03_grover_search.py` busca el número `11` entre 4
posibilidades y lo encuentra en el 100% de las corridas con una sola
"pregunta" al oráculo.

---

## 🧠 Capítulo 5: El primer truco de magia (Deutsch-Jozsa)

Este fue el **primer** truco cuántico de la historia que se demostró
más rápido que *cualquier* truco clásico. Así de importante.

El juego: te dan una caja misteriosa con una regla secreta. La regla
es de uno de dos tipos:

- **Constante:** siempre responde lo mismo (siempre 0, o siempre 1).
- **Balanceada:** responde 0 la mitad de las veces y 1 la otra mitad.

Con una computadora normal, en el peor caso tendrías que probar la caja
muchísimas veces para estar seguro. Con la cuántica: **una sola vez**.
Una. Siempre.

No sirve para nada práctico (es un juego inventado), pero demostró algo
gigante: *existen problemas donde lo cuántico es fundamentalmente
superior*. Fue la chispa que encendió todo el campo.

**En el proyecto:** `04_deutsch_jozsa.py` prueba los dos tipos de caja y
las clasifica perfecto, con una sola consulta cada una.

---

## 🖥️ Capítulo 6: ¿Y dónde está la computadora cuántica?

Aquí viene lo bonito: **no necesitas una**. Los 4 experimentos corren
en un **simulador** — un programa normal que finge ser cuántico. Es
como practicar fútbol en un videojuego antes de pisar la cancha real.

Cuando quieras jugar en la cancha real, IBM presta computadoras
cuánticas de verdad **gratis** (quantum.ibm.com). El código del proyecto
está escrito para que cambiar del simulador al hardware real sea una
sola línea. En hardware real los resultados salen un poquito "borrosos"
por el ruido — y pelear contra ese ruido es exactamente lo que estudia
la **ingeniería cuántica**.

---

## 🚀 Capítulo 7: Por qué la ingeniería molecular y QUANTUM

Esto no es "me gusta lo cuántico" como dice todo el mundo. Esto es:
*"Construí un laboratorio de 4 experimentos cuánticos en Qiskit, los
validé en simulador, y este es el repositorio."*

Pasión demostrada, no prometida. ⚛️

---

## ▶️ Cómo correrlo (para el niño curioso que hay en ti)

```bash
# 1. Crea tu cajita de herramientas (solo la primera vez)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. ¡Magia!
bash run_all.sh
```

Verás los circuitos dibujados, los resultados, y al final de cada
experimento un "OK" que significa: *la física funcionó como predice
la teoría*. 🎉
