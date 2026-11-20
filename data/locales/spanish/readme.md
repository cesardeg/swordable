# Translation Glossary & Style Guide: Sword & Sworcery EP — Spanish (`es-419`)

> **Global Reference:** This guide covers **Neutral Latin American Spanish (`es-419`)** terminology, grammar, dialect standards, and localization decisions for [`dialog.tsv`](dialog.tsv) and [`strings.tsv`](strings.tsv). For engine-wide technical constraints, universal translation philosophy, base character archetypes, and the full cross-language cultural allusions guide, see the **[Global Localization Guide](../readme.md)**.

---

## Purpose & Scope

This document serves as the **authoritative Spanish (`es-419`) reference** for *Superbrothers: Sword & Sworcery EP*. It pairs with the [Global Localization Guide](../readme.md) and documents:

1. **Normative Spanish Master Glossary (§1–§8):** Canonical terminology for characters, locations, items, gameplay mechanics, lore, moon cycles, UI/system labels, and idioms.
2. **Grammar, Voice & Dialect Standards (§9–§11):** Spanish-specific style rules, character voice nuances, and Neutral Latin American (`es-419`) pan-Hispanic conventions.
3. **Spanish Technical Implementations, Editorial Decisions & Cultural Adaptations (§12–§14):** Concrete Spanish implementations of engine/UI constraints, deliberate transcreation rationales, and pop-culture adaptations.

### Target Audience
- Spanish translators, editors, and QA testers
- LQA/MQM auditors evaluating linguistic compliance and technical playability
- Community contributors, modders, and documentation writers

### Usage Guidelines
- **Mandatory terms** are marked with ✅ and must be used exactly as specified
- **Context-dependent** terms are marked with ⚠️ and include usage notes
- **Creative alternatives** are provided where multiple valid options exist
- All terms reflect **post-correction standards** verified against [`spanish/dialog.tsv`](dialog.tsv), [`spanish/strings.tsv`](strings.tsv), and in-game builds

---

## Table of Contents
1. [Characters & NPCs](#characters--npcs)
2. [Locations & Places](#locations--places)
3. [Items & Objects](#items--objects)
4. [Gameplay Mechanics](#gameplay-mechanics)
5. [Story & Lore Concepts](#story--lore-concepts)
6. [Moon Phases & Cycles](#moon-phases--cycles)
7. [UI & System Terms](#ui--system-terms)
8. [Expressions & Idioms](#expressions--idioms)
9. [Grammar & Style Guidelines (`es-419`)](#grammar--style-guidelines-es-419)
10. [Character Voice & Tone (Spanish Nuances)](#character-voice--tone-spanish-nuances)
11. [Dialect & Regional Standards (`es-419`)](#dialect--regional-standards-es-419)
12. [Spanish Technical Implementations & LQA Reference](#spanish-technical-implementations--lqa-reference)
13. [Editorial Deviations & Transcreation Rationale (`es-419`)](#editorial-deviations--transcreation-rationale-es-419)
14. [Cultural Adaptations (`es-419`)](#cultural-adaptations-es-419)
15. [Quick Reference: Top 20 Critical Terms](#quick-reference-top-20-critical-terms)
16. [Spanish Translation Philosophy](#spanish-translation-philosophy)
17. [Version History](#version-history)
18. [Contributors & License](#contributors--license)

---

## Characters & NPCs

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **The Scythian (heroine)** | La Escita | ✅ Player character. Retains capitalized article as a substantivized protagonist name (`a La Escita`, `de La Escita`). |
| **Scythians (demonym / tribe)** | los escitas / escita | ✅ Demonym for the Scythian people. |
| **Logfella** | Tronquero | ✅ The woodcutter. See [Spanish Translation Philosophy](#spanish-translation-philosophy). |
| **Girl / Samae** | Samae | ✅ Always `"Samae"` after introduction |
| | La chica de cabello oscuro | First appearance description |
| **The Archetype** | El Arquetipo | ✅ The guide character (contracts as `del Arquetipo` after prepositions) |
| **Dogfella** | Perrero | ✅ The dog. See [Spanish Translation Philosophy](#spanish-translation-philosophy). |
| **Jim Guthrie** | Jim Guthrie | ✅ Never translate proper name |
| **The Grizzled Boor** | El Patán Canoso | ✅ Antagonist (contracts as `al Patán Canoso` in running prose) |
| **Andre (The Giant)** | André 'El Gigante' | ✅ Ghost character, maintain single quotes |
| **The Gogolithic Mass** | la Masa Gogolítica | ✅ The deathless specter (lowercase article in running prose per RAE norms) |

---

## Locations & Places

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **Mingi Taw** | Mingi Taw | ✅ Main mountain |
| **The Caucasus** | el Cáucaso | ✅ Geographic region |
| **Scythia** | Escitia | ✅ Homeland region |
| **The Perilous Precipice** | el Precipicio Peligroso | ✅ Major location |
| **Trigon Grove** | Claro Trigónico | ✅ Clearing |
| **The Moon Grotto** | la Gruta Lunar | ✅ Secret location |
| **The Kingdom of the Cloud** | el Reino de la Nube | ✅ Mingi Taw's title |
| | | |
| **stone hut** | choza de piedra | ⚠️ Logfella's dwelling |
| **stone wall** | muro de piedra | ✅ Blocks the old road |
| **meadow** | prado | ✅ Starting area |
| **deepwater pond** | estanque profundo | ✅ Natural Romance postpositive order |
| **old road** | antiguo camino | ✅ Never `"viejo"` |
| **log bridge** | puente de troncos | ✅ |
| **the whirling infinite** | el Infinito Arremolinado | ✅ Summit gateway |

### Sublocations

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| stone shelter | refugio de piedra | |
| mountain temple | templo de la montaña | |
| iron gate of the meadow | portón de hierro del prado | |
| cavernous cave of the meadow | cueva cavernosa del prado | |
| miracle of the meadow | milagro del prado | |
| titanic hollow tree | árbol hueco titánico | ✅ Postpositive adjective order (natural Romance syntax) |
| parliament of trees | parlamento de árboles | ✅ Lowercase metaphor (`a parliament of trees`), not a proper noun |

---

## Items & Objects

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **The Megatome** | el Megatomo | ✅ The burdensome book (lowercase article in running prose) |
| **sword** | espada | ✅ |
| **shield** | escudo | ✅ |
| **key** | llave | ✅ Logfella's lost key |
| | | |
| **Gold Trigon** | Trigón Dorado | ✅ First trigon |
| **Bright Moon Trigon** | Trigón de la Luna Radiante | ✅ Pink/bright trigon |
| **Dark Moon Trigon** | Trigón de la Luna Sombría | ✅ Blue/dark trigon |
| **The Trigon Trifecta** | la Tríada Trigónica | ✅ All three trigons (lowercase article in running prose) |
| | | |
| hearth | fuego / hogar | ⚠️ `hogar` used in poetic/proverbial contexts |
| firewood | leña | ✅ |
| well | pozo | ✅ |
| nestbox | casita de pájaros | ✅ Matches visual birdhouse pixel art (`D079`, `D108–D109`, `D338`) |
| mushroom | hongo | ✅ |
| record | disco | ✅ |

---

## Gameplay Mechanics

### Core Mechanics

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **Sworcery** | espadancia | ✅ Lowercase as common noun (magic/science). Cap only in Title/Intro. |
| **sworcerer** | espadancista | ✅ Practitioner of sworcery (`D280`, `D282`). Gender-invariable (`-ista`). |
| **Song of Sworcery** | Canción de Espadancia | ✅ Main ability (Proper noun) |
| **sworcery aura** | aura de espadancia | ✅ Visual indicator |
| **sylvan sprite** | espíritu silvano | ✅ Collectible creatures |
| **sonorous spume** | susurrantes espumas | ✅ Sprite indicators |
| **skyward beam** | haz celestial | ✅ Trigon activation |
| **miracle** | milagro | ✅ Special events |
| **to enact / work a miracle** | obrar un milagro | ✅ |

### Combat & Actions

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| press & hold / touch & hold | mantén presionado | ✅ Primary interaction |
| tap / tip tap | presiona / tip tap (`TOCAR` on `CNTRL_TOUCH`) | ✅ Quick button press (`TOCAR` for Switch touchscreen diagram `CNTRL_TOUCH`; `toca` in narrative prose) |
| swipe | desliza | ✅ Gesture |
| move it move it | mover el bote (`D035`) / apretar el paso (`D041`, `D321`) | ✅ Musical *Madagascar* nod in `D035`; natural haste/flight idiom in `D041` and `D321` |
| shield button | botón del escudo | ✅ With article |
| hold shield to heal (`HOLD_SHIELD_TO_HEAL`) | MANTÉN PARA CURARTE | ✅ Deliberate omission of `"shield"` to prevent horizontal collision with the sword sprite (*see [§12](#spanish-technical-implementations--lqa-reference)*) |
| swing sword | blande la espada / golpea con la espada | ✅ |
| dodge/evade | esquivar | ✅ |

### Game States

| English | Spanish (`es-419`) |
|---------|--------------------|
| dream-walking (Narrator) | paseos oníricos |
| dream-walking (Character) | caminar en sueños |
| threshold of liminality | umbral de la liminalidad |
| twilight realm | reino crepuscular |
| time of miracles | tiempo de milagros |

---

## Story & Lore Concepts

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **woeful errand** | funesto cometido | ✅ The Scythian's quest |
| **martyrdom** | martirio | ✅ The Scythian's fate |
| **deathless specter** | espectro inmortal | ✅ The Gogolithic Mass |
| **heebie jeebies** | los pelos de punta | ✅ Physical sensation of fear |
| **cosmic friends forever** | amigos cósmicos para siempre | ✅ Ending phrase |
| **for glory & for spite** | por la gloria y por pura terquedad | ✅ Deliberate adaptation: in English gaming idiom, doing something `"out of spite / for spite"` means stubborn defiance (`"por pura terquedad"`), whereas Spanish *por despecho* carries an unintended romantic/heartbreak connotation (*mal de amores*) |
| **time of woe** | tiempo de angustia | ✅ Session II Theme (mirrors *tiempo de milagros*) |
| | | |
| linguistic thought transmission | transmisión de pensamiento lingüístico | ✅ |
| esoteric markings | símbolos esotéricos | ✅ Unified across `D142`, `D210`, and `D238` (Megatome contents) |
| oblique insight | visión oblicua | ✅ The Archetype's clues |
| mythopoetic psychocosmology | psicocosmología mitopoética | ✅ |
| set and setting | Disposición y Entorno | ✅ Adapted concepts |

### Atmospheric Terms

| English | Spanish (`es-419`) |
|---------|--------------------|
| loathsome rainbow | odioso arcoíris |
| sinister storm / sworcery | siniestra tormenta / espadancia |
| grim pole / flagpole / mysteries | lúgubre poste / mástil / lúgubres misterios |
| ominous statue / beat | estatua ominosa / ominoso ritmo |
| eerie song | espeluznante canción |
| gathering storm | inminente tormenta |
| haunted darkness | oscuridad embrujada |

---

## Moon Phases & Cycles

### Critical: Always use definite articles in Spanish!

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| **The Bright Moon looms** | **La** Luna Radiante **resplandece** | ✅ ALWAYS with article |
| **The Dark Moon reigns** | **La** Luna Sombría **reina** | ✅ ALWAYS with article |
| crescent moon | luna creciente | ✅ |
| mood/humor of the moon | el humor de la luna | ✅ |
| lunar cycle | ciclo lunar | ✅ |

### Usage Patterns

- ✅ `"Mientras **la** Luna Radiante resplandece"`
- ✅ `"Mientras **la** Luna Sombría reina"`
- ❌ Never: `"Mientras Luna Radiante resplandece"` (missing article)

### Verb Conjugations

| Phase | Spanish Verb |
|-------|--------------|
| Bright Moon | `resplandece` (present) / `resplandecía`, `resplandeciera`, `resplandecerá` (past/future) |
| Dark Moon | `reina` (present) / `reinaba`, `reinaría` (past narrative) |

---

## UI & System Terms

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| Session I, II, III | Sesión I, II, III | ✅ |
| Side A / Side B | Lado A / Lado B | ✅ |
| press play | presiona 'Jugar' | ✅ |
| equip | equipa | ✅ |
| scroll down | desplázate | ✅ Concise imperative for Megatome tutorial |
| unsheathe / rotate | ¿DESENVAINAR? / ¿ROTAR? | ✅ |
| BELIEVE | CONFÍA | ✅ UI Action prompt |
| QUIT? (`QUIT` / `EXIT`) | SALIR | ✅ Constrained to 5 chars on `QUIT` slide-out tab (*see [§12](#spanish-technical-implementations--lqa-reference)*) |

### Menu/System

| English | Spanish (`es-419`) |
|---------|--------------------|
| Settings | AJUSTES |
| date & time | fecha y hora |
| Go Home? | ¿INICIO? |
| Authorized Personnel Only | Solo personal autorizado |

---

## Expressions & Idioms

### Hashtags

| English | Spanish (`es-419`) |
|---------|--------------------|
| #helloworld | #holamundo |
| #obviously | #obvio |
| #gotmegatome | #tengomegatomo |
| #miracles | #milagros |
| #woodchopping | #leñando |
| #yes #no #maybe | #si #no #quizas |
| #woe | #angustia |
| #wetboots | #botasmojadas |
| #loathsomerainbows | #odiososarcoiris |
| #slaughter | #masacre |

### Colloquialisms

| English | Spanish (`es-419`) | Notes |
|---------|--------------------|-------|
| amirite? | ¿En serio? / ¿no crees? | ✅ Context: Exasperation vs Rhetorical agreement |
| Whoa | Vaya / Espera... ¿qué? / ¡¿Cómo?! | ✅ Context dependent |
| Yikes! | ¡Caramba! | ✅ Ghost vs Archetype |
| Hmm... | Hmm... | ✅ Keep as is |
| cool | genial / buena gente | ⚠️ Context: Situation vs Person |

### Character-Specific Speech

**Dogfella / Perrero:**
- English: `"Bark Bark Bark"`
- Spanish: `"Guau Guau Guau"`
- ✅ Maintain barking sound appropriate to Spanish

---

## Grammar & Style Guidelines (`es-419`)

> For cross-language rules shared across all localizations, see [Universal Style Guidelines](../readme.md#translation-philosophy--universal-style-guidelines).

### 1. **Article Usage with Moons**
- ✅ ALWAYS use **"la"** before Luna Radiante/Sombría.
- ✅ `"**la** Luna Radiante **resplandece**"`
- ✅ `"**la** Luna Sombría **reina**"`

### 2. **Verb Choice for Moons**
- Bright Moon → **"resplandece"** (shines/glows vividly in the sky).
- Dark Moon → **"reina"** (reigns).
- Creates intentional visual vs. sovereign contrast between the two moons.

### 3. **"Heebie Jeebies" / Fear Translation**
- Standard: **"los pelos de punta"** (heebie jeebies) ✅
- Alternate: **"manojo de nervios"** (freaking out)
- Never mix within the same context.

### 4. **Old Road**
- ✅ **"antiguo camino"** (always).
- ❌ `"viejo camino"` (never — sounds too colloquial).

### 5. **Formatting & Capitalization**
- Trigon names: **"Trigón Dorado"** (both words capitalized)
- Location & item names: **"el Precipicio Peligroso"**, **"la Gruta Lunar"**, **"el Megatomo"**, **"la Masa Gogolítica"**, **"la Tríada Trigónica"** (proper nouns capitalized; preceding definite article in lowercase in running prose per RAE orthography, contracting normally as `al` / `del`)
- Protagonist & character titles: **"La Escita"** retains its capitalized article as a substantivized protagonist name (`a La Escita`, `de La Escita`), whereas descriptive epithets contract naturally in prose (`al Patán Canoso`, `del Arquetipo`).
- Moon phases: **"Luna Radiante"** / **"Luna Sombría"** (both capitalized, preceded by lowercase article `la`)

### 6. **Majestic Plural & Gender Agreement (`Plural Mayestático`)**
- **Context:** The Scythian uses the majestic plural `"we"` (`"nosotros"`) throughout her narration.
- **Rule:** When an adjective modifies this `"we"`, the masculine/neuter plural form (e.g., `listos`, `cansados`) must be used, even though The Scythian is female.
- **Rationale:** This is a critical stylistic choice to preserve player immersion. The `"we"` is intentionally ambiguous, representing both The Scythian and the player. Using the feminine plural (`listas`) would break this connection for non-female players. The masculine plural acts as a gender-neutral form, ensuring all players feel included in the narrative.
- ✅ **Correct:** `...cómo nos habíamos vuelto tan listos.`
- ❌ **Incorrect:** `...cómo nos habíamos vuelto tan listas.`

### 7. **Conjunctions vs. English Ampersands (`y` / `+` instead of `&`)**
- ✅ **Natural Conjunctions:** Replace the English stylistic `&` with the standard Spanish conjunction **`y`** across all UI prompts (`MANTÉN Y DESLIZA`, `APUNTAR Y HACER CLIC`), ancient signs (`Escitia, Cimeria, Asiria y Persia`), and narrative prose.
- ✅ **Button Combinations:** Use **`+`** for simultaneous controller button prompts (`PRESIONA L + R`).
- ✅ **Brand Exception:** Retain `&` exclusively in the game's proper title and official abbreviations (`Superbrothers: Sword & Sworcery EP`, `S:S&SEP`, `S&S`).
- 💡 **Trigon Collections:** Trigon collection achievements use a deadpan, two-sentence structure (`Domamos el Trigón Dorado. Somos lo máximo.`) to match the dry humor of the English source.

### 8. **Postpositive Adjective Order (`árbol hueco titánico`)**
- ✅ ALWAYS place descriptive adjectives after the noun in natural Romance syntax: **"árbol hueco titánico"** / **"árbol titánico"**.
- ❌ NEVER use the English anteposition calque: `"titánico árbol hueco"` / `"titánico árbol"`.

### 9. **Narrative Imperfect vs. Inchoative Expressions of Sensation**
- ✅ Use the imperfect (*pretérito imperfecto*: `teníamos la sensación`, `esperaba`, `conectaba`, `sabíamos`, `supusimos`) when establishing continuous scene backdrops, mental states, and ongoing impressions (e.g., `D094`: `we had a feeling` → `teníamos la sensación`).
- ✅ When the English source marks a sudden, punctual onset (`D347` / `D352`: `We got that/the peculiar feeling`), use expressive inchoative verbs (`Nos invadió la/esa extraña sensación`) rather than the flat calque `tuvimos la sensación`.
- ❌ Avoid abrupt preterite calques (`tuvimos la sensación`, `esperó`, `conectó`) when describing continuous background states.

### 10. **Gender-Neutral Player Treatment in Spanish**
While **La Escita** is consistently feminine in narrative prose, **The Player** addressed by The Archetype avoids gender-marked adjectives or participles via five techniques (*see [Global Guide](../readme.md#translation-philosophy--universal-style-guidelines)*):
1. **Nominalization over participles:** `¿Confusión?` instead of `¿Confundido/a?`.
2. **Invariable adjectives:** `Eres especial` (invariable in gender).
3. **Verbal circumlocutions:** `si te pierdes o sientes confusión` instead of `si te encuentras perdido/a`.
4. **Epicene nouns:** `personas compasivas y razonables` to avoid masculine/feminine splits.
5. **Impersonal UI & prompts:** `¿Todo listo?` instead of `¿Listo/a?`; `¿Confirmas que quieres activar...?`.

### 11. **Cursor vs. Puntero & Hashtag Rules**
- **Cursor vs. Puntero:** Use **`CURSOR`** for the on-screen visual reticle (`MOVER CURSOR`, `CENTRAR CURSOR`), and **`PUNTERO` / `APUNTAR`** for the physical Joy-Con pointing device or aiming action (`SENSIBILIDAD DEL PUNTERO`, `APUNTAR Y HACER CLIC`).
- **Hashtags:** Translate and culturally adapt hashtags (`#holamundo`, `#obvio`, `#threegutrecordsx100pre`, `#odiososarcoiris`, `#trigondomado`). Omit acute accents on vowels (`#si`, `#quizas`, `#trigondomado`, `#masfacildelopensado`) to reflect authentic 2011 Twitter behavior, while preserving **`ñ`** (`#leñando`, `#bañomutante`).
- **Retro Media Terms:** Adapt quirky media phrasing naturally (`Side B` → `Lado B`, `press play` → `presiona 'Jugar'`).

### 12. **UI Box & Fixed-Width HUD Constraints**
- Honor fixed HUD/slide-out character budgets (`HOLD_SHIELD_TO_HEAL`, `QUIT`, `SETTINGS`, `GO_HOME`). *See [§12](#spanish-technical-implementations--lqa-reference) and [Global Technical Constraints](../readme.md#technical-ui--engine-constraints-lqa-reference--post-mortem).*
- **3-Line Tweet Box Heuristic:** Aim to keep playable dialogue lines (`D001–D580`) near or under **~140 characters** as a practical length heuristic. Because the engine uses proportional bitmap fonts (`conduit_itc_2x.fnt`, `arial_narrow.fnt`), wrapping is governed by pixel width rather than exact character count.

### Verb Strategy for `"We spied..."`

To avoid repetition of the verb `"avistar"`, use a flexible set of synonyms based on the context of the observation:

| Observation Type | Spanish (`es-419`) Verbs | Usage Context |
|:---|:---|:---|
| **General Sighting (Default)** | `avistamos`, `vimos` | The base verb for a neutral observation or the first in a series. |
| **Discovery / Surprise** | `descubrimos`, `hallamos`, `encontramos` | For finding something new, hidden, or important (e.g., a secret statue). |
| **Chance Encounter** | `nos topamos con` | For stumbling upon an object or character unexpectedly. |
| **Focused Observation** | `observamos`, `notamos` | For looking at something more closely or noticing a subtle detail. |
| **Distant / Difficult Sighting** | `distinguimos` | For seeing something far away, in the dark, or in a crowd. |

**Rule of Thumb:** In a sequence of observations in the same area (e.g., `INFO_CABIN*`), vary the verbs to reflect the process of discovery. Start with a general `avistamos` and move to more specific verbs like `notamos` or `descubrimos`. Apply the same variation logic to common verbs like `"conseguir"` (`got`), `"decir"` (`said`), and `"pensar"` (`thought`).

---

## Character Voice & Tone (Spanish Nuances)

> For the base English archetype definitions, see [Global Character Voice & Tone](../readme.md#character-voice--tone).

| Character | Spanish Name | Spanish Nuances |
|-----------|--------------|-----------------|
| **The Scythian** | La Escita | **Narradora Épica y Cansada.** Usa el plural mayestático (`"nosotros"`). Suena como la protagonista de una saga antigua, pero con un monólogo interior moderno y sarcástico (`"uf. ¿Otra misión de búsqueda? ¿En serio?"`). |
| **The Archetype** | El Arquetipo | **El Guía Erudito.** Su lenguaje es formal, casi académico. Usa palabras complejas y conceptos abstractos (`"psicocosmología mitopoética"`). Rompe la cuarta pared, dirigiéndose al jugador como un participante en un experimento. |
| **Logfella** | Tronquero | **El Leñador Práctico.** Habla de forma sencilla y directa. Es amigable pero rudo. No es `"mucho de historias"` y prefiere lo práctico (cortar leña). Su apodo `"Tronquero"` refleja un carácter rústico y cercano. |
| **Girl (Samae)** | Samae | **La Observadora Gentil.** Su tono es inocente, curioso y melancólico. Está conectada con lo místico (espíritus, sueños). Habla con una sencillez poética, en contraste con la complejidad del Arquetipo. |
| **Dogfella** | Perrero | **El Can Críptico.** Ladra (`"Guau"`), pero sus pensamientos son sorprendentemente filosóficos o graciosos. El nombre `"Perrero"` lo vincula con el estilo de `"Tronquero"`. |
| **The Grizzled Boor** | El Patán Canoso | **El Antagonista Silencioso.** No tiene diálogos. Su amenaza se percibe a través de las descripciones de La Escita. Su nombre `"El Patán Canoso"` debe sonar intimidante. |
| **Ghosts** | Fantasmas / Espíritus | **Los Espíritus Expositivos.** Cada fantasma cuenta su tragedia. Su tono es de lamento, arrepentimiento o, a veces, dicen `"tonterías inútiles"` irritantes. Son vehículos para la historia del mundo. |

---

## Dialect & Regional Standards (`es-419`)

The Spanish localization is anchored in **Neutral Latin American Spanish (`es-419`)**, designed to feel native across the Americas while remaining completely natural and intelligible to players in Spain (`es-ES`):

- **Pronouns & Forms of Address:** Uses `tú` for singular address and `ustedes` / `los` for plural (`* * * LOS QUEREMOS MUCHÍSIMO * * *`), avoiding Peninsular `vosotros / os` as well as regional *voseo* (`vos`).
- **Verb Tense & Syntax:**
  - Uses the simple preterite (*pretérito perfecto simple*: `¿Qué pasó?`, `¿Adónde fue a parar mi llave?`, `recuperaste`) for immediate past actions rather than the Peninsular compound perfect (`¿Qué ha pasado?`, `¿Adónde se ha ido?`).
  - Uses transitive `informar que` (`Me acaban de informar que...`) in accordance with educated Latin American usage rather than Peninsular `informar de que`.
- **Console & UI Terminology (First-Party `es-419` Standards):**
  - Action prompts use **`PRESIONA` / `PRESIONAR` / `MANTÉN PRESIONADO`** for button actions (aligned with Nintendo Switch, PlayStation, and Xbox LatAm standards) rather than Peninsular `PULSA` / `MANTÉN PULSADO`, while reserving **`TOCAR`** for touchscreen tap gestures (`CNTRL_TOUCH`).
  - Hardware, settings, and media terms follow Nintendo of America / LatAm `es-419` conventions: **`CONTROL`** (not `mando`), **`PALANCA` / `PALANCAS`** for Switch thumbsticks (not `joystick` / `analógico`), **`RESTABLECER`** for settings reset (`RESET`, distinct from `¿REINICIAR?` for `START_OVER`), **`COMPUTADORAS`** (not `ordenadores`), and **`LADO A / LADO B`** for vinyl/cassette sides (not `Cara A / Cara B`).
- **Lexical Neutrality:** Avoids country-specific idioms or Peninsularisms in dialogue (e.g., `misión de búsqueda` instead of Peninsular `misión de recadero`; `¡No lo puedo creer!` instead of Peninsular `¡No me lo puedo creer!`; `pájaro enojado` instead of `enfadado`; `descifrar` instead of Peninsular `desvelar` [= reveal]; `clima` and `detenerme` instead of Peninsular `tiempo` [= weather] and `pararme` [= stop]).

---

## Spanish Technical Implementations & LQA Reference

> For the underlying engine behavior, sprite-collision diagnostics, Switch/PC/iOS test evidence, and Capybara Games developer notes, see [Global Technical, UI & Engine Constraints](../readme.md#technical-ui--engine-constraints-lqa-reference--post-mortem).

### 1. Fixed-Width HUD & Menu Implementations (`strings.tsv`)

| Row & Key | English Source | Spanish (`es-419`) | Length & Technical Rationale |
|-----------|----------------|--------------------|------------------------------|
| `S127` (`HOLD_SHIELD_TO_HEAL`) | `HOLD SHIELD TO HEAL` | `MANTÉN PARA CURARTE` | **19 chars.** Omits `"EL ESCUDO"` (which would be 29 chars and crash into the vertical sword sprite); the pulsing shield icon directly below makes the referent self-evident. |
| `S099` (`QUIT`) | `QUIT?` | `SALIR` | **5 chars (hard cap: 5).** Inverted question marks (`¿SALIR?`, 7 chars) crash through the circular button icon (`¿SALI⊗?`). |
| `S133` (`SETTINGS`) | `SETTINGS` | `AJUSTES` | **7 chars.** Avoids `CONFIGURACIÓN` (13 chars), which collided with the sliders icon (`CONFIGURA[≡]ÓN`) in the official European `ES_FIGS` release. |
| `S029` (`GO_HOME`) | `GO HOME?` | `¿INICIO?` | **8 chars (cap: 8).** Unreferenced prototype string; inverted question marks cause no in-game collision. |
| `S113` (`EXIT`) | `EXIT` | `SALIR` | **5 chars.** Desktop PC display/graphics options only; separate UI hierarchy from `QUIT` (`S099`). |
| `S130` (`MOTION_CURSOR_SENSITIVITY`) | `MOTION CURSOR SENSITIVITY` | `SENSIBILIDAD: CURSOR POR MOVIMIENTO` | **35 chars.** Retains `CURSOR` to prevent confusion with Joy-Con motion/walking speed while fitting Switch slider width. |
| `S131` (`STICK_CURSOR_SENSITIVITY`) | `STICK CURSOR SENSITIVITY` | `SENSIBILIDAD: CURSOR CON PALANCA` | **32 chars.** Uses Nintendo LatAm first-party term `PALANCA`. |
| `S177` (`POINTCLICK_CURSORSENS_NINSWITCH`) | `POINT & CLICK CURSOR SENSITIVITY` | `SENSIBILIDAD: APUNTAR Y HACER CLIC` | **34 chars.** Structured colon prefix avoids the 45-char overflow of `SENSIBILIDAD DEL CURSOR DE APUNTAR Y HACER CLIC`. |

### 2. Bitmap Font Glyph Registration (`strings.tsv`)
- **`DIGIT_STRING` (`S126`):** `0123456789` (retains leading `0` stripped in `strings.en.tsv`).
- **`SPANISH_SPECIAL` (`S167`):** `Á á É é Í í Ó ó Ú ú Ñ ñ Ü ü ¿ ¡ º ª « » ‹ › €` (expands the uppercase-only Switch source to include lowercase Spanish accented vowels, `ñ`, and `ü`; do not revert).

### 3. Multi-Platform `strings.tsv` Superset (Rows 230–236)
`spanish/strings.tsv` retains **236 lines** (vs. 229 in Switch `strings.en.tsv`) to preserve binary schema & key-index compatibility across Switch, PC/Steam, and legacy iOS builds (*see [Global Guide](../readme.md#5-multi-platform-stringstsv-superset-236-lines-vs-229-lines-in-switch-stringsentsv--binary-schema--key-index-compatibility)*):

| Row | Key / ID | Official Capybara Games English Source | Spanish (`es-419`) | Context & Platform |
|:---:|---|---|---|---|
| **230** | `TWITTER_SELECT_BUTTON` | `SELECT` | `SELECCIONAR` | iOS Twitter account selection modal button |
| **231** | `TWITTER_SELECT_MSG` | `PLEASE SELECT A TWITTER ACCOUNT` | `"POR FAVOR, SELECCIONA UNA CUENTA DE TWITTER"` | iOS Twitter dialog prompt |
| **232** | `TWITTER_NO_ACCOUNTS` | `There are no Twitter accounts configured on this device.` | `No hay cuentas de Twitter configuradas en este dispositivo.` | iOS system account check message |
| **233** | `TWITTER_REQUESTING` | `REQUESTING ACCESS...` | `SOLICITANDO ACCESO...` | iOS OAuth/permission modal status |
| **234** | `TAP_QUESTION` | `TAP?` | `¿PRESIONAR?` | iOS/Mobile touch tutorial prompt |
| **235** | `EXIT_TITLE` | `Exit #sworcery?` | `¿Salir de #espadancia?` | PC / Steam exit confirmation dialog title |
| **236** | `EXIT_PROMPT` | `Are you sure you want to exit?` | `¿De verdad quieres salir?` | PC / Steam exit confirmation dialog body |

### 4. Cross-Platform & Parity Lines (`dialog.tsv`)
- **`ARCHETYPE_TREEHINT` (`D230`, 140 chars):**
  `Al entonar la Canción de Espadancia, desliza con suma suavidad el aura para mirar alrededor (o acerca el cursor al borde o usa las flechas).`
  *(Makes aura-dragging the primary universal instruction for iOS/iPadOS & PC, followed by desktop cursor-edge/arrow controls.)*
- **`ARCHETYPE_GROTTOPARADOX` (`D494`, dead-code parity):**
  `Una vez que el humor de la luna ha sido alterado en la Gruta Lunar, la`
  *(Retained truncated at Line 494 solely for exact `dialog.tsv` row parity.)*

### 5. Quotes, Period Placement & Acronym Formatting
- **Straight ASCII Single Quotes (`'...'`):** Always use `'...'` for internal citations, nicknames (`André 'El Gigante'`), and UI prompts (`presiona 'Jugar'`) due to bitmap font glyph limits and TSV escaping. Keep legacy outer CSV quotes on `S090`, `S219`, `S231`.
- **Quotation-Mark Period Placement:** Inline citations embedded inside surrounding narration (`D011`, `D020`, `D132`) place the closing period **outside** the quotes per RAE *Ortografía* (2010, §3.4.8.2.2) (`"...".` / `'...'.`), whereas standalone full-utterance quoted transmissions and carved signs (`D004–D005`, `D068–D071`, `D081–D086`, `D145–D189`, `D531`) **intentionally keep the closing period inside the quotation marks** (`"..."`) to mirror the English TSV framing (`"""..."""`) as a consistent retro dialogue-box convention.
- **Unified Acronym:** Always use compact **`S:S&SEP`** (never `S:S&S EP`).

---

## Editorial Deviations & Transcreation Rationale (`es-419`)

Unlike [§12](#spanish-technical-implementations--lqa-reference), the entries below are **purely linguistic, narrative, and stylistic editorial decisions**—not technical limitations of the game engine:

### 1. `SCYTHIAN_FOUNDATION` (`dialog.tsv` Line 508) — Narrative Slip Correction (`singular / plural`)
- **Source (`en`):** `Wait... why am I referring to myself in first person? I thought our story was told in second person? #editingoversight`
- **Spanish (`es-419`):** `Espera... ¿por qué hablo en singular? ¿No se supone que la historia va en plural? #erratadeedicion`
- **Rationale:** The English writer accidentally confused *"first-person plural"* (`we / our`) with *"second person"* (`you`). Translating literally (`primera persona / segunda persona`) breaks the meta-joke because `"nuestra historia"` is first-person plural. Contrasting **`en singular` / `en plural`**—as the official 8-4 Japanese localization did—restores the intended fourth-wall joke.

### 2. Direct-Speech Explicitación & Quote Punctuation (`D145–D146`, `D150–D151`, `D156–D167`, `D170–D175`, `D178`, `D181–D182`, `D184–D185`, `D187`, `D189`, `D531`)
- **Pattern:** Spanish adds literal double quotation marks (`"""..."""`) to direct-speech dialogue blocks spoken by ghosts/spirits (e.g., `D145`, `D150`, `D156`, `D170`, `D181`) and Samae's dream (`D531`), where the English script displays no rendered quotation marks (`D176–D177` remain unquoted because they are third-person indirect narration by The Scythian).
- **Rationale:** As documented in [Source-Script Lore Notes](../readme.md#known-source-script-quirks--lore-notes), ghosts project silent telepathic *"linguistic thought-transmissions"* in lore. Adding literal double quotes in Spanish is **not correcting a Capybara Games typo**—it is an **intentional stylistic explicitación** for Spanish readers, providing immediate visual clarity when a ghost's first-person singular voice (`yo`) alternates against The Scythian's surrounding first-person plural narration (`nosotros`). Standalone quoted boxes intentionally keep the closing period inside the quotes (`"..."`), while inline quotations (`D011`, `D020`, `D132`) follow RAE *Ortografía* (2010) with the period outside (`"...".` / `'...'.`).

### 3. `ARCHETYPE_GOLDMASTERINTRO` (`dialog.tsv` Line 283) — Creative Cultural License & Register Shift
- **Source (`en`):** `Confused? Excellent. Keep calm & carry on.`
- **Spanish (`es-419`):** `¿Confusión? Calma, calma, ¡que no panda el cúnico!`
- **Rationale:** Although The Archetype is normally formal and academic, this line is an **explicitly acknowledged creative license and register break**: just as the English script pivots from arcane psychocosmology into a ubiquitous British cultural meme (*"Keep calm & carry on"*), the Spanish localization substitutes Roberto Gómez Bolaños's (*El Chapulín Colorado*) iconic pan-Latin American catchphrase for immediate fourth-wall comedic impact.

---

## Cultural Adaptations (`es-419`)

> For full cultural context, historical background, and cross-language guidance for every allusion below, see the **[Global Cultural References Guide](../readme.md#cultural-references-pop-culture-homages--literary-allusions)**.

### 1. Cinema & Television

| Row & ID | English Source | Reference | Spanish (`es-419`) Adaptation |
|---|---|---|---|
| `D103` (`INFO_WELLWHITESTAG`) | `LONG LIVE THE NEW FLESH` | *Videodrome* (1983) | `LARGA VIDA A LA NUEVA CARNE` |
| `D108` (`INFO_NESTBOX`) | `...now home to a wretched hive.` | *Star Wars: A New Hope* (1977) | `... ahora era hogar de una colmena de escoria y villanía.` |
| `D132` (`INFO_ROCKSHOWGIRL`) | `...she said fire walk with me.` | *Twin Peaks* (1990–1992) | `... 'Fuego, camina conmigo'.` |
| `D375–D376` (`GCLUE_LAKESHORELAKE`) | `...I don't speak log-language.` / `...owls are not what they seem...` | *Twin Peaks* (Log Lady & The Giant) | `... no hablo tronqués.` / `... a veces los búhos no son lo que parecen...` |
| `D558–D560` (`LOGFELLA_CRESCENTWANE`) | `...immortals from space who sparked in mankind...` | *2001: A Space Odyssey* (1968) | Translated with solemn, mythic-scientific phrasing (`seres inmortales del espacio que despertaron en la humanidad...`). |

### 2. Music, Street Art & Comics

| Row & ID | English Source | Reference | Spanish (`es-419`) Adaptation |
|---|---|---|---|
| `D004` (`SIGN_TADPOL`) | `"""Home is where the hearth is."" #threegutrecords4ever"` | Three Gut Records + *heart/hearth* pun | `"""Donde el fuego alumbra, el hogar se vislumbra."" #threegutrecordsx100pre"` |
| `D035` | `...to move it move it move it.` | *"I Like to Move It"* / *Madagascar* (2005) | `¡y a mover, mover el bote!` *(Note: `D041` & `D321` use natural haste idiom `apretar el paso`.)* |
| `D127` (`INFO_CABINRECORD`) | `#theballadofthespacebabies` | Jim Guthrie OST flagship track | Kept as `#theballadofthespacebabies` |
| `D170` (`GRAVE_MEADOWGHOST*`) | `...Andre The Giant assembled a posse...` | André the Giant / Shepard Fairey | `André 'El Gigante' juntó a su gente...` |
| `D250`, `D418` (`ARCHETYPE_MEADOWHINT`, `MIRACLE1_MOUNTAINMEADOW`) | `...fold-in abilities of the great wizard Al Jaffee.` | Al Jaffee & *MAD* Fold-Ins | `los milagrosos poderes de plegado del gran mago Al Jaffee` |
| `D355` (`GCLUE_MOUNTAINMEADOW`) | `...what a dog's gotta do do.` | Turntable skip + *do-do* pun | `... lo que un perro tiene que ha-ha-hacer.` |
| `D404`, `D405` (`JIM_LOGFELLATHOUGHTS`) | `#1000songs` / `#andwegotolder` | Jim Guthrie discography | Kept as `#1000songs` and `#andwegotolder` |
| `D412` (`LOGFELLA_MOONGROTTOCOMMENT`) | `It's a long way from 0 to 1 & if an alien said hello it'd be in cryptic code on the stereo. Wait... what?` | Jim Guthrie – *"Hands in My Pocket"* | `Del 0 al 1 hay un largo trecho, y si un alien nos dijera 'hola', sería mediante un código críptico por el estéreo. Espera... ¿qué?` |

### 3. Videogames & Tech Culture

| Row & ID | English Source | Reference | Spanish (`es-419`) Adaptation |
|---|---|---|---|
| `D002` (`GIRL_TONGUES`) | `#helloworld` | Programming `"Hello, World!"` | `#holamundo` |
| `D006`, `D038` (`SIGN_CHASM`, `LOGFELLA_PRECIPICE_DONE`) | `...skyward sword...` | *Zelda: Skyward Sword* (2010 reveal) | `... una espada alzada al cielo...` |
| `D089`, `D098`, `D251` (`INFO_BIRDEYESCULPTURE`, `ARCHETYPE_MEADOWHINT`) | `...angry bird sculpture... #subtlereference` | *Angry Birds* (2009) | `... un pájaro enojado... #sutilreferencia` |
| `D308`, `D311–D319` | `...upload The Megatome...` | Cloud computing pun (*Kingdom of the Cloud*) | `subir el Megatomo` / `subimos el Megatomo` |
| `D675` (`CREDITS`) | `S:S&S EP is a link to the past.` | *Zelda: A Link to the Past* (1991) | `S:S&SEP es un 'Link' al pasado.` |
| `D683` (`CREDITS`) | `...originally going to be called 'Poopsock'...` | MMORPG `"Poopsock"` slang | `S:S&SEP iba a llamarse 'Poopsock' originalmente. Esto es totalmente cierto.` |

### 4. Literature, Philosophy, Politics & Folklore

| Row & ID | English Source | Reference | Spanish (`es-419`) Adaptation |
|---|---|---|---|
| `D101–D102` (`INFO_UNWELLWELL`, `INFO_WELLNESS`) | `The well seemed unwell.` / `All's well that ends well.` | Shakespeare (c. 1604) | `El pozo soltó un sollozo. #pozo #sollozo` / `Bien está lo que bien acaba.` |
| `D234` (`ARCHETYPE_MUSHROOMHINT`) | `It has even been asserted that divinatory mushrooms...` | Terence McKenna (*Stoned Ape*) | `Incluso se ha postulado que los hongos adivinatorios pudieron haber tenido un papel clave en el desarrollo de la psique humana.` |
| `D283` (`ARCHETYPE_GOLDMASTERINTRO`) | `Confused? Excellent. Keep calm & carry on.` | British poster → *El Chapulín Colorado* | `¿Confusión? Calma, calma, ¡que no panda el cúnico!` |
| `D372–D373`, `D383` (`GCLUE_*`) | `...known unknowns & the unknown unknowns.` / `unknown nouns` | Donald Rumsfeld (2002) | `Hay dos tipos de incógnitas: las incógnitas conocidas y las incógnitas desconocidas.` / `... los sustantivos incógnitos...` |
| `D599` (`CREDITS`) | `...leadership & strategery...` | *SNL* / Will Ferrell (2000) | `... liderazgo y estrategería...` |
| `D674` (`CREDITS`) | `...Robert E. Howard's sword and sorcery stories...` | Robert E. Howard | `... las historias de espada y hechicería de Robert E. Howard.` |
| `D678` (`CREDITS`) | `...Carl G. Jung & his fascinating ""Red Book""...` | Carl G. Jung (*Liber Novus*) | `... Carl G. Jung y su fascinante 'Libro Rojo'...` |

---

## Quick Reference: Top 20 Critical Terms

| # | English | Spanish (`es-419`) |
|---|---------|--------------------|
| 1 | The Scythian | La Escita |
| 2 | Sworcery | Espadancia |
| 3 | The Megatome | El Megatomo |
| 4 | sylvan sprite | espíritu silvano |
| 5 | The Bright Moon looms | La Luna Radiante resplandece |
| 6 | The Dark Moon reigns | La Luna Sombría reina |
| 7 | woeful errand | funesto cometido |
| 8 | Logfella | Tronquero |
| 9 | Mingi Taw | Mingi Taw |
| 10 | The Gogolithic Mass | La Masa Gogolítica |
| 11 | Trigon Trifecta | Tríada Trigónica |
| 12 | sonorous spume | susurrantes espumas |
| 13 | dream-walking | paseos oníricos / caminar en sueños |
| 14 | the whirling infinite | Infinito Arremolinado |
| 15 | press & hold / touch & hold | mantén presionado |
| 16 | Perilous Precipice | Precipicio Peligroso |
| 17 | old road | antiguo camino |
| 18 | stone hut | choza de piedra |
| 19 | deepwater pond | estanque profundo |
| 20 | heebie jeebies | los pelos de punta |

---

## Spanish Translation Philosophy

> For the four overarching translation pillars and general naming strategy, see [Global Translation Philosophy](../readme.md#translation-philosophy--universal-style-guidelines).

### Neologism: `espadancia`
- Treated as a lowercase common noun (like *magia* or *ciencia*), capitalized only in the title/intro or the proper noun **`Canción de Espadancia`**.
- The `-ancia` suffix (like `constancia`, `elegancia`) gives `"espadancia"` an abstract, psionic, and philosophical quality—matching the game's description of sworcery as a *"consciousness expansion technique"* rather than conventional magic.
- Practitioner form: **`espadancista`** (gender-invariable `-ista`, used in `D280`, `D282`).

### Character Names: `Tronquero` & `Perrero`
- **`Logfella` → `Tronquero`:** Combining `Tronco` + `-ero` creates a rustic, descriptive nickname reflecting the character's profession that sounds like an authentic *apodo de pueblo*.
- **`Dogfella` → `Perrero`:** Creates an exact parallel to `"Tronquero"` using the same `-ero` suffix. In this rustic context it clearly evokes *"the dog guy / the one with the dog"*, and is more pan-Hispanically universal and sonically stronger than regional alternatives like `"Chuchero"`.

---

## Version History

- **v1.0–v1.2** (2024) — Initial glossary creation, post-correction standards, and Spanish grammar guidelines.
- **v1.3–v1.7** (2026) — Cross-lingual harmonization, in-game HUD collision LQA pass (`HOLD_SHIELD_TO_HEAL`, `QUIT`, `SETTINGS`, `SENSITIVITY`), `SPANISH_SPECIAL` glyph registration (Row 167), multi-platform 236-row `strings.tsv` superset, `ARCHETYPE_TREEHINT` cross-platform bridge, cultural guide, and separation of technical constraints from editorial deviations.
- **v1.8** (2026) — Comprehensive MQM/LQA audit pass for `es-419`: standardized Nintendo Switch thumbstick terminology to first-party `palanca/palancas` (`S131`, `S136`, `S171`, `S181`, `S188`, `S205`, `S215`), shortened `CNTRL_TOUCH` → `TOCAR`, disambiguated `RESET` → `RESTABLECER` and `SLAY` → `¿MATAR?`, synchronized `S232`/`S236` and `D230` (140 chars), added `espadancista` (`sworcerer`), corrected major ES findings (`nosequé` → `artilugio`, `D138` tense harmony, `D184` restored `espíritus silvanos`, Peninsularisms `desvelar`/`tiempo`/`pararme`, `D517/520/524/539` possessives, `D680` false friend `crudo` → `rudimentario`), aligned punctual recent-past verbs to `es-419` simple preterite, unified RAE punctuation/ellipses/credits, and explicitly documented the deliberate dialogue-box quotation-period convention.
- **v1.9** (2026) — Standardized cross-lingual glossary terms in `es-419`: `the whirling infinite` (`D157–D558` + `D444`) → `el Infinito Arremolinado`, `deepwater pond` → `estanque profundo`, `nestbox` → `casita de pájaros`, `The Bright Moon looms` → `la Luna Radiante resplandece`, and `move it move it` (`D041`/`D321`) → `apretar el paso`.
- **v2.0** (2026) — Split the monolithic `data/locales/readme.md` into dedicated per-language documentation (`spanish/readme.md` and `portuguese/readme.md`) paired with the global technical and cultural reference in [`../readme.md`](../readme.md).

---

## Contributors & License

- **Original game text:** Superbrothers Inc., Capy Games, Jim Guthrie
- **Spanish (`es-419`) localization:** [cesardeg](https://github.com/cesardeg)

For questions, corrections, or additions to this glossary, please submit issues to the repository.

This translation glossary is provided as reference documentation for the *Superbrothers: Sword & Sworcery EP* localization project. Usage rights follow the game's original licensing terms.
