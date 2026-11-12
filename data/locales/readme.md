# Translation Glossary: Sword & Sworcery EP
## English → Spanish (ES-419) / Portuguese (PT-BR)

---

## Purpose & Architecture of This Document

This document serves as the **authoritative reference** for Superbrothers: Sword & Sworcery EP across Neutral Latin American Spanish (`es-419`) and Brazilian Portuguese (`pt-BR`) localizations. It is structured into three distinct operational components:

1. **Normative Translation Style Guide & Master Glossary (§1–§9):**
   - Standardized canonical terminology across all game text.
   - Character names, locations, and key concepts.
   - Creative adaptations, neologisms, and dialectal guidelines.
2. **Technical Constraints & LQA Post-Mortem (§10):**
   - Documents strictly empirical technical constraints: UI sprite collisions, bitmap font limits, schema key preservation, and cross-platform input differences backed by in-engine testing and Capybara Games' developer notes.
3. **Editorial Deviations & Transcreation Rationale (§11) & Cultural Guide (§12):**
   - Transparently separates creative, linguistic, and literary localization decisions (such as fourth-wall wordplay corrections, direct-speech explicitación, and pop-culture transcreations) from engine constraints.

### Target Audience
- Translators, localization teams, and QA testers
- LQA auditors evaluating compliance and technical playability
- Community translators, modders, and documentation writers

### Usage Guidelines
- **Mandatory terms** are marked with ✅ and must be used exactly as specified
- **Context-dependent** terms are marked with ⚠️ and include usage notes
- **Creative alternatives** are provided where multiple valid options exist
- All terms reflect **post-correction standards** verified against actual `.tsv` files and in-game builds

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
9. [Grammar & Style Guidelines](#grammar--style-guidelines)
10. [Technical, UI & Engine Constraints (LQA Reference & Post-Mortem)](#technical-ui--engine-constraints-lqa-reference--post-mortem)
11. [Editorial Deviations & Transcreation Rationale](#editorial-deviations--transcreation-rationale)
12. [Cultural References, Pop-Culture Homages & Literary Allusions (Cross-Language Guide)](#cultural-references-pop-culture-homages--literary-allusions-cross-language-guide)

---

## Characters & NPCs

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **The Scythian (heroine)** | La Escita | A Citiana | ✅ Player character. In PT, "A Citiana" is preserved to avoid homophonic clash with cita/citar. |
| **Scythians (demonym / tribe)** | los escitas / escita | os citas / cita | ✅ Demonym for the Scythian people. PT regularized to "citas / cita". |
| **Logfella** | Tronquero | Troncadeiro | ✅ The woodcutter. See Philosophy section. |
| **Girl / Samae** | Samae | Samae | ✅ Always "Samae" after introduction |
| | La chica de cabello oscuro | A garota de cabelos escuros | First appearance description |
| **The Archetype** | El Arquetipo | O Arquétipo | ✅ The guide character (contracts as `del Arquetipo` / `do Arquétipo` after prepositions) |
| **Dogfella** | Perrero | Cachorreiro | ✅ The dog. See Philosophy section. |
| **Jim Guthrie** | Jim Guthrie | Jim Guthrie | ✅ Never translate proper name |
| **The Grizzled Boor** | El Patán Canoso | O Patife Grisalho | ✅ Antagonist (contracts as `al Patán Canoso` / `o Patife Grisalho` in running prose) |
| **Andre (The Giant)** | André 'El Gigante' | André, 'O Gigante' | ✅ Ghost character, maintain quotes |
| **The Gogolithic Mass** | la Masa Gogolítica | a Massa Gogolítica | ✅ The deathless specter (lowercase article in running prose per RAE/PT norms) |

---

## Locations & Places

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **Mingi Taw** | Mingi Taw | Mingi Taw | ✅ Main mountain |
| **The Caucasus** | el Cáucaso | o Cáucaso | ✅ Geographic region |
| **Scythia** | Escitia | Cítia | ✅ Homeland region |
| **The Perilous Precipice** | el Precipicio Peligroso | o Precipício Perigoso | ✅ Major location |
| **Trigon Grove** | Claro Trigónico | Clareira Trigônica | ✅ ES: clearing, PT: grove clearing |
| **The Moon Grotto** | la Gruta Lunar | a Gruta Lunar | ✅ Secret location |
| **The Kingdom of the Cloud** | el Reino de la Nube | o Reino da Nuvem | ✅ Mingi Taw's title |
| | | | |
| **stone hut** | choza de piedra | cabana de pedra | ⚠️ Logfella's dwelling |
| **stone wall** | muro de piedra | muro de pedra | ✅ Blocks the old road |
| **meadow** | prado | campina | ✅ Starting area |
| **deepwater pond** | insondable estanque | insondável lagoa | ✅ Adjective before noun (Epic tone) |
| **old road** | antiguo camino | antigo caminho | ✅ ES: Never "viejo". PT: Never "estrada velha" |
| **log bridge** | puente de troncos | ponte de toras | ✅ |
| **the whirling infinite** | el Arremolinado Infinito | o Remoinhado Infinito | ✅ Summit gateway |

### Sublocations

| English | Spanish (ES) | Portuguese (PT-BR) |
|---------|--------------|-------------------|
| stone shelter | refugio de piedra | abrigo de pedra |
| mountain temple | templo de la montaña | templo da montanha |
| iron gate of the meadow | portón de hierro del prado | portão de ferro da campina |
| cavernous cave of the meadow | cueva cavernosa del prado | caverna cavernosa na campina |
| miracle of the meadow | milagro del prado | milagre da campina |
| titanic hollow tree | árbol hueco titánico | árvore oca titânica | ✅ Postpositive adjective order (natural Romance syntax) |
| parliament of trees | parlamento de árboles | parlamento de árvores | ✅ Lowercase metaphor (`a parliament of trees`), not a proper noun |

---

## Items & Objects

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **The Megatome** | el Megatomo | o Megatomo | ✅ The burdensome book (lowercase article in running prose) |
| **sword** | espada | espada | ✅ |
| **shield** | escudo | escudo | ✅ |
| **key** | llave | chave | ✅ Logfella's lost key |
| | | | |
| **Gold Trigon** | Trigón Dorado | Trígono Dourado | ✅ First trigon |
| **Bright Moon Trigon** | Trigón de la Luna Radiante | Trígono da Lua Radiante | ✅ Pink/bright trigon |
| **Dark Moon Trigon** | Trigón de la Luna Sombría | Trígono da Lua Sombria | ✅ Blue/dark trigon |
| **The Trigon Trifecta** | la Tríada Trigónica | a Tríade Trigônica | ✅ All three trigons (lowercase article in running prose) |
| | | | |
| hearth | fuego / hogar | fogo / lareira / lar | ⚠️ `hogar` / `lareira / lar` used in poetic/proverbial contexts |
| firewood | leña | lenha | ✅ |
| well | pozo | poço | ✅ |
| nestbox | curioso nido / nido | curioso ninho / ninho | ✅ |
| mushroom | hongo | cogumelo | ✅ |
| record | disco | disco | ✅ |

---

## Gameplay Mechanics

### Core Mechanics

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **Sworcery** | espadancia | espadância | ✅ Lowercase as common noun (magic/science). Cap only in Title/Intro. |
| **Song of Sworcery** | Canción de Espadancia | Canção da Espadância | ✅ Main ability (Proper noun) |
| **sworcery aura** | aura de espadancia | aura de espadância | ✅ Visual indicator |
| **sylvan sprite** | espíritu silvano | espírito silvano | ✅ Collectible creatures. |
| **sonorous spume** | susurrantes espumas | sussurrantes espumas | ✅ Sprite indicators. |
| **skyward beam** | haz celestial | feixe celestial | ✅ Trigon activation. PT: "feixe" not "raio" |
| **miracle** | milagro | milagre | ✅ Special events |
| **to enact / work a miracle** | obrar un milagro | operar um milagre | ✅ PT: Always "operar" (or "farão um milagre" in rhyme); NEVER "obrar" due to scatological ambiguity |

### Combat & Actions

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| press & hold / touch & hold | mantén presionado | mantenha pressionado / segure | ✅ Primary interaction |
| tap / tip tap | presiona / tip tap | pressione / tip tap | ✅ Quick touch (`toca` / `toque` in narrative prose) |
| swipe | desliza | deslize | ✅ Gesture |
| move it move it | mover el bote | remexer | ✅ Fast movement, colloquial |
| shield button | botón del escudo | botão do escudo | ✅ With article |
| hold shield to heal (`HOLD_SHIELD_TO_HEAL`) | MANTÉN PARA CURARTE | SEGURE PARA SE CURAR | ✅ Deliberate omission of `"shield"` to prevent horizontal collision with the sword sprite (*see §10.1*) |
| swing sword | blande la espada / golpea con la espada | branda a espada / rebata com a espada | ✅ |
| dodge/evade | esquivar | esquivar | ✅ |

### Game States

| English | Spanish (ES) | Portuguese (PT-BR) |
|---------|--------------|-------------------|
| dream-walking (Narrator) | paseos oníricos | caminhadas oníricas |
| dream-walking (Character) | caminar en sueños | caminhar em sonhos |
| threshold of liminality | umbral de la liminalidad | limiar da liminaridade |
| twilight realm | reino crepuscular | reino crepuscular |
| time of miracles | tiempo de milagros | tempo de milagres |

---

## Story & Lore Concepts

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **woeful errand** | funesto cometido | funesta missão | ✅ The Scythian's quest |
| **martyrdom** | martirio | martírio | ✅ The Scythian's fate |
| **deathless specter** | espectro inmortal | espectro imortal | ✅ The Gogolithic Mass |
| **heebie jeebies** | los pelos de punta | frio na espinha | ✅ Physical sensation of fear |
| **cosmic friends forever** | amigos cósmicos para siempre | amigos cósmicos para sempre | ✅ Ending phrase |
| **for glory & for spite** | por la gloria y por pura terquedad | pela glória e por pura teimosia | ✅ Deliberate adaptation: in English gaming idiom, doing something "out of spite / for spite" means stubborn defiance ("por pura terquedad / teimosia"), whereas Spanish *por despecho* carries an unintended romantic/heartbreak connotation (*mal de amores*) |
| **time of woe** | tiempo de angustia | tempo de angústia | ✅ Session II Theme (mirrors *tiempo de milagros* / *tempo de milagres*) |
| | | | |
| linguistic thought transmission | transmisión de pensamiento lingüístico | transmissão de pensamento linguístico | ✅ |
| esoteric markings | símbolos esotéricos | símbolos esotéricos | ✅ Unified across `D142`, `D210`, and `D238` (Megatome contents) |
| oblique insight | visión oblicua | visão oblíqua | ✅ The Archetype's clues |
 | mythopoetic psychocosmology | psicocosmología mitopoética | psicocosmologia mitopoética | ✅ |
 | set and setting | Disposición y Entorno | Preparação e Ambiente | ✅ Adapted concepts |

### Atmospheric Terms

| English | Spanish (ES) | Portuguese (PT-BR) |
|---------|--------------|-------------------|
| loathsome rainbow | odioso arcoíris | odioso arco-íris |
| sinister storm / sworcery | siniestra tormenta / espadancia | sinistra tempestade / espadância |
| grim pole / flagpole / mysteries | lúgubre poste / mástil / lúgubres misterios | lúgubre poste / mastro / lúgubres mistérios |
| ominous statue / beat | estatua ominosa / ominoso ritmo | estátua ominosa / ritmo ominoso |
| eerie song | espeluznante canción | arrepiante canção |
| gathering storm | inminente tormenta | iminente tempestade |
| haunted darkness | oscuridad embrujada | trevas assombradas |

---

## Moon Phases & Cycles

### Critical: Always use definite articles in Spanish & Portuguese!

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| **The Bright Moon looms** | **La** Luna Radiante **impera** | **A** Lua Radiante **paira** | ✅ ALWAYS with article |
| **The Dark Moon reigns** | **La** Luna Sombría **reina** | **A** Lua Sombria **reina** | ✅ ALWAYS with article |
| crescent moon | luna creciente | lua crescente | ✅ |
| mood/humor of the moon | el humor de la luna | o humor da lua | ✅ |
| lunar cycle | ciclo lunar | ciclo lunar | ✅ |

### Usage Patterns

**Spanish:**
- ✅ "Mientras **la** Luna Radiante impera"
- ✅ "Mientras **la** Luna Sombría reina"
- ❌ Never: "Mientras Luna Radiante impera" (missing article)

**Portuguese:**
- ✅ "Enquanto **a** Lua Radiante paira"
- ✅ "Enquanto **a** Lua Sombria reina"
- ❌ Never: "Enquanto Lua Sombria reina" (missing article)

### Verb Conjugations

| Phase | Spanish Verb | Portuguese Verb |
|-------|--------------|-----------------|
| Bright Moon | impera (present) / imperaba, imperara (past narrative) | paira (present) / pairava, pairasse (past narrative) |
| Dark Moon | reina (present) / reinaba, reinaría (past narrative) | reina (present) / reinava, reinaria (past narrative) |

---

## UI & System Terms

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| Session I, II, III | Sesión I, II, III | Sessão I, II, III | ✅ |
| Side A / Side B | Lado A / Lado B | Lado A / Lado B | ✅ |
| press play | presiona 'Jugar' | pressione 'Jogar' | ✅ |
| equip | equipa | equipe | ✅ |
| scroll down | desplázate | role | ✅ Concise imperative for Megatome tutorial |
| unsheathe / rotate | ¿DESENVAINAR? / ¿ROTAR? | DESEMBAINHAR? / GIRAR? | ✅ |
| BELIEVE | CONFÍA | ACREDITE | ✅ UI Action prompt |
| QUIT? (`QUIT` / `EXIT`) | SALIR | SAIR? / SAIR | ✅ Constrained to 5 chars on `QUIT` slide-out tab (*see §10.2*) |

### Menu/System

| English | Spanish (ES) | Portuguese (PT-BR) |
|---------|--------------|-------------------|
| Settings | AJUSTES | AJUSTES |
| date & time | fecha y hora | data e hora |
| Go Home? | ¿INICIO? | INÍCIO? |
| Authorized Personnel Only | Solo personal autorizado | Apenas Pessoal Autorizado |

---

## Expressions & Idioms

### Hashtags

| English | Spanish (ES) | Portuguese (PT-BR) |
|---------|--------------|-------------------|
| #helloworld | #holamundo | #olamundo |
| #obviously | #obvio | #obvio |
| #gotmegatome | #tengomegatomo | #tenhomegatomo |
| #miracles | #milagros | #milagres |
| #woodchopping | #leñando | #lenhando |
| #yes #no #maybe | #si #no #quizas | #sim #nao #talvez |
| #woe | #angustia | #angustia |
| #wetboots | #botasmojadas | #botasmolhadas |
| #loathsomerainbows | #odiososarcoiris | #odiososarcoiris |
| #slaughter | #masacre | #matanca |

### Colloquialisms

| English | Spanish (ES) | Portuguese (PT-BR) | Notes |
|---------|--------------|-------------------|-------|
| amirite? | ¿En serio? / ¿no crees? | Fala sério, né? / não acha? | ✅ Context: Exasperation vs Rhetorical agreement |
| Whoa | Vaya / Espera... ¿qué? / ¡¿Cómo?! | Nossa / Eita | ✅ Context dependent |
| Yikes! | ¡Caramba! | Credo! / Caramba! | ✅ Ghost vs Archetype |
| Hmm... | Hmm... | Hmm... | ✅ Keep as is |
| cool | genial / buena gente | legal / incrível | ⚠️ Context: Person vs Situation |

### Character-Specific Speech

**Dogfella/Cachorreiro:**
- English: "Bark Bark Bark"
- Spanish: "Guau Guau Guau"
- Portuguese: "Au Au Au"
- ✅ Maintain barking sound appropriate to language

---

## Grammar & Style Guidelines

### Spanish (ES) Style Rules

#### 1. **Article Usage with Moons**
- ✅ ALWAYS use **"la"** before Luna Radiante/Sombría.
- ✅ "**la** Luna Radiante **impera**"
- ✅ "**la** Luna Sombría **reina**"

#### 2. **Verb Choice for Moons**
- Bright Moon → **"impera"** (dominates/reigns supreme).
- Dark Moon → **"reina"** (reigns).
- Creates intentional contrast between the two moons

#### 3. **"Heebie Jeebies" / Fear Translation**
- Standard: **"los pelos de punta"** (heebie jeebies) ✅
- Alternate: **"manojo de nervios"** (freaking out)
- Never mix within same context

#### 4. **Old Road**
- ✅ **"antiguo camino"** (always).
- ❌ "viejo camino" (never - sounds too colloquial)

#### 5. **Formatting & Capitalization**
- Trigon names: **"Trigón Dorado"** (both words capitalized)
- Location & item names: **"el Precipicio Peligroso"**, **"la Gruta Lunar"**, **"el Megatomo"**, **"la Masa Gogolítica"**, **"la Tríada Trigónica"** (proper nouns capitalized; preceding definite article in lowercase in running prose per RAE orthography, contracting normally as `al` / `del`)
- Protagonist & character titles: **"La Escita"** retains its capitalized article as a substantivized protagonist name (`a La Escita`, `de La Escita`), whereas descriptive epithets contract naturally in prose (`al Patán Canoso`, `del Arquetipo`).
- Moon phases: **"Luna Radiante"** / **"Luna Sombría"** (both capitalized, preceded by lowercase article `la`)

#### 6. **Majestic Plural & Gender Agreement (`Plural Mayestático`)**
- **Context:** The Scythian uses the majestic plural "we" ("nosotros") throughout her narration.
- **Rule:** When an adjective modifies this "we," the masculine/neuter plural form (e.g., `listos`, `cansados`) must be used, even though The Scythian is female.
- **Rationale:** This is a critical stylistic choice to preserve player immersion. The "we" is intentionally ambiguous, representing both The Scythian and the player. Using the feminine plural (`listas`) would break this connection for non-female players. The masculine plural acts as a gender-neutral form, ensuring all players feel included in the narrative.
- ✅ **Correct:** `...cómo nos volvimos tan listos.`
- ❌ **Incorrect:** `...cómo nos volvimos tan listas.`

#### 7. **Conjunctions vs. English Ampersands (`y` / `+` instead of `&`)**
- ✅ **Natural Conjunctions**: Replace the English stylistic `&` with the standard Spanish conjunction **`y`** across all UI prompts (`MANTÉN Y DESLIZA`, `APUNTAR Y HACER CLIC`), ancient signs (`Escitia, Cimeria, Asiria y Persia`), and narrative prose.
- ✅ **Button Combinations**: Use **`+`** for simultaneous controller button prompts (`PRESIONA L + R`).
- ✅ **Brand Exception**: Retain `&` exclusively in the game's proper title and official abbreviations (`Superbrothers: Sword & Sworcery EP`, `S:S&SEP`, `S&S`).
- 💡 **Trigon Collections**: Trigon collection achievements use a deadpan, two-sentence structure (`Domamos el Trigón Dorado. Somos lo máximo.`) to match the dry humor of the English source.

#### 8. **Postpositive Adjective Order (`árbol hueco titánico`)**
- ✅ ALWAYS place descriptive adjectives after the noun in natural Romance syntax: **"árbol hueco titánico"** / **"árbol titánico"**.
- ❌ NEVER use the English anteposition calque: `"titánico árbol hueco"` / `"titánico árbol"`.

#### 9. **Narrative Imperfect vs. Inchoative Expressions of Sensation**
- ✅ Use the imperfect (*pretérito imperfecto*: `teníamos la sensación`, `esperaba`, `conectaba`, `sabíamos`, `supusimos`) when establishing continuous scene backdrops, mental states, and ongoing impressions (e.g., `D094`: `we had a feeling` → `teníamos la sensación` / `tínhamos a sensação`).
- ✅ When the English source marks a sudden, punctual onset (`D347` / `D352`: `We got that/the peculiar feeling`), use expressive inchoative verbs (`Nos invadió la/esa extraña sensación` in ES; `Sentimos a/essa estranha sensação` in PT) rather than the flat calque `tuvimos la sensación`.
- ❌ Avoid abrupt preterite calques (`tuvimos la sensación`, `esperó`, `conectó`) when describing continuous background states.

#### 10. **UI Box & Fixed-Width HUD Constraints**
- Honor fixed HUD/slide-out character budgets (`HOLD_SHIELD_TO_HEAL`, `QUIT`, `SETTINGS`, `GO_HOME`). *For full sprite-collision evidence, character budgets, and menu hierarchy analysis, see §10.1–§10.2.*
- **3-Line Tweet Box Heuristic**: Aim to keep playable dialogue lines (`D001–D580`) near or under **~140 characters** as a practical length heuristic. Because the engine uses proportional bitmap fonts (`conduit_itc_2x.fnt`, `arial_narrow.fnt`), wrapping is governed by pixel width rather than exact character count (*see §10.10*).

---

### Portuguese (PT-BR) Style Rules

#### 1. **Article Usage with Moons**
- ✅ ALWAYS use **"a"** before Lua Radiante/Sombria.
- ✅ "Enquanto **a** Lua Radiante paira"
- ✅ "Enquanto **a** Lua Sombria reina"
- ❌ **NEVER**: "Enquanto Lua Sombria reina" (grammatically incorrect)

#### 2. **Verb Choice for Moons (`paira` vs `reina`)**
- ✅ Use **"paira"** for *Lua Radiante* and **"reina"** for *Lua Sombria* in present-tense milestone prompts (`Enquanto a Lua Radiante paira` / `Enquanto a Lua Sombria reina`), inflecting naturally (`pairava`, `pairasse`, `reinava`, `reinaria`) in narrative past and subordinate contexts.

#### 3. **Lagoa vs Lago**
- **"insondável lagoa"** = deepwater pond (small body of water)
- **"lago"** = lake (large body of water)
- These are NOT interchangeable

#### 4. **"Hearth" Translation Context**
- **"fogo"** = fire (standard narrative and dialogue references)
- **"lareira / lar"** = hearth (formal/poetic contexts)
- Special phrase: **"Onde a lareira arde, o lar faz alarde"** ✅ (Poetic wordplay using rhyme and meter).

#### 5. **Conjunctions vs. English Ampersands (`e` / `+` instead of `&`)**
- ✅ **Natural Conjunctions**: Replace the English stylistic `&` with the standard Portuguese conjunction **`e`** across all UI prompts (`SEGURE E DESLIZE`, `APONTAR E CLICAR`), ancient signs (`Cítia, Ciméria, Assíria e Pérsia`), and narrative prose.
- ✅ **Button Combinations**: Use **`+`** for simultaneous controller button prompts (`PRESSIONE L + R`).
- ✅ **Brand Exception**: Retain `&` exclusively in the game's proper title and official abbreviations (`Superbrothers: Sword & Sworcery EP`, `S:S&SEP`, `S&S`).
- 💡 **Trigon Collections**: Trigon collection achievements use a deadpan, two-sentence structure (`Domamos o Trígono Dourado. Somos os maiores.`) to match the dry humor of the English source.

#### 6. **Formatting & Capitalization**
- Trigon names: **"Trígono Dourado"** (both words capitalized)
- Location names: **"O Precipício Perigoso"** (proper noun)
- Moon phases: **"Lua Radiante"** (both capitalized)

#### 7. **Postpositive Adjective Order (`árvore oca titânica`)**
- ✅ ALWAYS place descriptive adjectives after the noun in natural Romance syntax: **"árvore oca titânica"** / **"árvore titânica"**.
- ❌ NEVER use the English anteposition calque: `"titânica árvore oca"` / `"titânica árvore"`.

#### 8. **Eliminating Scatological Calques (`operar milagres`)**
- ✅ ALWAYS use **"operar milagres"** (or `"farão um milagre"` in the rhyming couplet).
- ❌ NEVER use `"obrar milagres"`: in modern spoken Portuguese (PT-BR and PT-PT), *obrar* strongly connotes defecation (*evacuar/fazer cocô*), turning holy miracles into unintended comedy.

#### 9. **Demonym Disambiguation (`A Citiana` vs. `citas`)**
- ✅ Protagonist: **"A Citiana"** (preserves distinct heroine identity and avoids homophonic collision with *cita* / *citar*).
- ✅ People / Tribe: **"citas / os citas"** (normalized demonym for the Scythian people).

#### 10. **UI Dialogue Line-Length Management**
- As a visual heuristic for the 3-line retro tweet boxes, keep row lengths roughly around ~42–46 characters and avoid long words near line boundaries to prevent single-word orphan overflow into a 4th line (e.g., Line 97: `...e a chave parecia perdida nos sonhos.` instead of wrapping `sonhos.` into a 4th row). Remember that wrapping is governed by pixel width in proportional bitmap fonts, so always verify visually in-game (*see §10.10*).

### Verb Strategy for "We spied..." (ES/PT)

To avoid repetition of the verb "avistar" (to spot/spy), we use a flexible set of synonyms based on the context of the observation. This creates a more dynamic and narrative tone.

| Observation Type | Spanish (ES) Verbs | Portuguese (PT) Verbs | Usage Context |
|:---|:---|:---|:---|
| **General Sighting (Default)** | `avistamos`, `vimos` | `avistamos`, `vimos` | The base verb for a neutral observation or the first in a series. |
| **Discovery / Surprise** | `descubrimos`, `hallamos`, `encontramos` | `descobrimos`, `encontramos` | For finding something new, hidden, or important (e.g., a secret statue). |
| **Chance Encounter** | `nos topamos con` | `nos deparamos com` | For stumbling upon an object or character unexpectedly. |
| **Focused Observation** | `observamos`, `notamos` | `observamos`, `notamos`, `reparamos em` | For looking at something more closely or noticing a subtle detail. |
| **Distant / Difficult Sighting**| `distinguimos` | `distinguimos` | For seeing something far away, in the dark, or in a crowd. |

**Rule of Thumb:** In a sequence of observations in the same area (e.g., `INFO_CABIN*`), vary the verbs to reflect the process of discovery. Start with a general `avistamos` and move to more specific verbs like `notamos` or `descubrimos`.

This same logic of variation is applied to other common verbs like "conseguir" (`got`), "decir" (`said`), and "pensar" (`thought`) to enrich the narrative voice of The Scythian.


---

## Character Voice & Tone

This section defines the personality and speaking style for each character to ensure consistency in dialogue across all languages.

| Character | Voice & Tone | Spanish Nuances | Portuguese Nuances |
|---|---|---|---|
| **The Scythian** | **The Stoic Narrator.** Uses "we" (plural majestatis). Her tone is epic, descriptive, and poetic, but with flashes of dry, modern humor and inner thoughts. She is on a "woeful errand" but often sounds cynical or unimpressed. | **Narradora Épica y Cansada.** Usa el plural mayestático ("nosotros"). Suena como la protagonista de una saga antigua, pero con un monólogo interior moderno y sarcástico ("uf. ¿Otra misión de búsqueda? ¿En serio?"). | **Narradora Épica e Cansada.** Usa o plural majestático ("nós"). Soa como a protagonista de uma saga antiga, mas com um monólogo interior moderno e sarcástico ("aff. Outra missão de busca? Fala sério, né?"). |
| **The Archetype** | **The Erudite Guide.** Speaks formally, almost academically. Uses complex, philosophical, and sometimes fourth-wall-breaking language ("mythopoetic psychocosmology"). He is the director of the "experience." | **El Guía Erudito.** Su lenguaje es formal, casi académico. Usa palabras complejas y conceptos abstractos ("psicocosmología mitopoética"). Rompe la cuarta pared, dirigiéndose al jugador como un participante en un experimento. | **O Guia Erudito.** Sua linguagem é formal, quase acadêmica. Usa palavras complexas e conceitos abstratos ("psicocosmologia mitopoética"). Quebra a quarta parede, tratando o jogador como um participante de um experimento. |
| **Logfella** | **The Practical Woodsman.** Simple, direct, and down-to-earth. He is friendly but gruff. He has a "low tolerance for lore" and is more concerned with practical matters like chopping wood and staying warm. His speech is colloquial. | **El Leñador Práctico.** Habla de forma sencilla y directa. Es amigable pero rudo. No es "mucho de historias" y prefiere lo práctico (cortar leña). Su apodo "Tronquero" refleja un carácter rústico y cercano. | **O Lenhador Prático.** Fala de forma simples e direta. É amigável, mas um pouco rude. Não é "muito de histórias" e prefere o pragmatismo (cortar lenha). Seu apelido "Troncadeiro" reflete sua natureza rústica. |
| **Girl (Samae)** | **The Gentle Observer.** Innocent, curious, and deeply connected to the mystical world (sprites, dreams, moon moods). Her tone is soft, sometimes melancholic ("feeling the woe"), and observant. | **La Observadora Gentil.** Su tono es inocente, curioso y melancólico. Está conectada con lo místico (espíritus, sueños). Habla con una sencillez poética, en contraste con la complejidad del Arquetipo. | **A Observadora Gentil.** Seu tom é inocente, curioso e melancólico. Está conectada com o místico (espíritos, sonhos). Fala com uma simplicidade poética, em contraste com a complexidade do Arquétipo. |
| **Dogfella** | **The Cryptic Canine.** Mostly barks, but his "barks" are translated into profound or humorous wisdom when The Scythian can understand him. His "voice" is surprisingly philosophical. | **El Can Críptico.** Ladra ("Guau"), pero sus pensamientos son sorprendentemente filosóficos o graciosos. El nombre "Perrero" lo vincula con el estilo de "Tronquero". | **O Cão Críptico.** Late ("Au"), mas seus pensamentos são surpreendentemente filosóficos ou humorísticos. O nome "Cachorreiro" o conecta ao estilo de "Troncadeiro". |
| **The Grizzled Boor**| **The Silent Antagonist.** He has no dialogue. His presence is communicated through actions and The Scythian's descriptions. He is menacing and brutish. | **El Antagonista Silencioso.** No tiene diálogos. Su amenaza se percibe a través de las descripciones de La Escita. Su nombre "El Patán Canoso" debe sonar intimidante. | **O Antagonista Silencioso.** Não tem diálogos. Sua ameaça é percebida pelas descrições da Citiana. Seu nome "O Patife Grisalho" deve soar intimidador. |
| **Ghosts** | **The Expositional Spirits.** Each ghost has a specific story to tell. Their tone is often sorrowful, regretful, or filled with unhelpful "nonsense." They serve to deliver lore about past events. | **Los Espíritus Expositivos.** Cada fantasma cuenta su tragedia. Su tono es de lamento, arrepentimiento o, a veces, dicen "tonterías inútiles" irritantes. Son vehículos para la historia del mundo. | **Os Espíritos Expositivos.** Cada fantasma conta sua tragédia. Seu tom é de lamento, arrependimento ou, às vezes, falam "baboseiras inúteis" irritantes. São veículos para a história do mundo. |

---

### Universal Style Guidelines (Both Languages)

#### 1. **Hashtags & Social Media Aesthetic**
- **Translate and culturally adapt hashtags**: All in-game hashtags are creatively localized into Spanish and Portuguese (e.g., `#holamundo` / `#olamundo`, `#obvio`, `#threegutrecordsx100pre` / `#threegutrecordsprasempre`, `#odiososarcoiris`, `#trigondomado` / `#trigonodomado`) to preserve the game's witty, meta-textual 2011 Twitter aesthetic for native audiences. (The original European FIGS release left hashtags untranslated in English, which broke immersion).
- Keep specific retro media terms when part of the game's quirky style (e.g., `Side B` → `Lado B`, `press play` → `presiona 'Jugar'` / `pressione 'Jogar'`).

#### 2. **Proper Nouns**
- Never translate: Jim Guthrie, André, Samae
- Character titles translate: "The Giant" → "El Gigante" / "O Gigante"

#### 3. **Emphasis & Tone**
- Maintain poetic/epic tone in narrative
- Keep casual tone in character dialogue
- Preserve humor and wordplay where possible

#### 4. **Neologisms**
- "Sworcery" is a core neologism - never use generic "magic"
- Spanish: **"Espadancia"** (espada + -ancia).
- Portuguese: **"Espadância"** (espada + -ância).

#### 5. **Consistency Over Variation**
- Use exact same term throughout for key concepts
- Variation acceptable only for:
  - Grammatical requirements (verb conjugations)
  - Avoiding repetition in same paragraph
  - Character voice differences

#### 6. **Gender-Neutral Player Treatment**
The game makes a strict distinction between:
- **The Scythian (The Protagonist):** A female warrior, consistently referred to with feminine grammar within the narrative (`La Escita` / `A Citiana`).
- **The Player (The Participant):** The real person addressed by The Archetype breaking the fourth wall. To maintain total immersion for all players, gender-marked adjectives or participles are strictly avoided through five core techniques:
  1. **Nominalization over participles:** e.g., `¿Confusión?` (ES) / `Confusão?` (PT-BR) instead of `¿Confundido/a?` / `Confuso/a?`.
  2. **Invariable adjectives:** e.g., `Eres especial` / `Você é especial` (invariable in gender).
  3. **Verbal circumlocutions:** e.g., `si te pierdes o sientes confusión` / `se você se perder ou sentir confusão` instead of `si te encuentras perdido/a`.
  4. **Epicene nouns:** e.g., `personas compasivas y razonables` / `pessoas compassivas e razoáveis` to avoid masculine/feminine splits.
  5. **Impersonal UI & prompts:** e.g., `¿Todo listo?` / `Tudo pronto?` instead of `¿Listo/a?`; `¿Confirmas que quieres activar...?` (ES) / `Tem certeza de que deseja ativar...?` (PT-BR).

#### 7. **Cursor vs. Pointer (Hardware vs. Visual)**
- **Cursor:** The visual reticle/element moving on screen (e.g., `MOVER CURSOR`, `CENTRAR CURSOR` / `CENTRALIZAR CURSOR`).
- **Pointer/Apuntar (ES: Puntero / PT: Ponteiro):** The physical Joy-Con acting as a pointing device, or the action of aiming it (e.g., `SENSIBILIDAD DEL PUNTERO` / `SENSIBILIDADE DO PONTEIRO`, `APUNTAR Y HACER CLIC` / `APONTAR E CLICAR`). Do NOT use "cursor" to refer to the hardware.

---

## Dialect & Regional Standards (`es-419` & `pt-BR`)

#### 1. **Spanish: Neutral Latin American (`es-419`) with Pan-Hispanic Accessibility**
The Spanish localization is anchored in **Neutral Latin American Spanish (`es-419`)**, designed to feel native across the Americas while remaining completely natural and intelligible to players in Spain (`es-ES`):
- **Pronouns & Forms of Address:** Uses `tú` for singular address and `ustedes` / `los` for plural (`* * * LOS QUEREMOS MUCHÍSIMO * * *`), avoiding Peninsular `vosotros / os` as well as regional *voseo* (`vos`).
- **Verb Tense & Syntax:**
  - Uses the simple preterite (*pretérito perfecto simple*: `¿Qué pasó?`, `¿Adónde fue a parar mi llave?`, `recuperaste`) for immediate past actions rather than the Peninsular compound perfect (`¿Qué ha pasado?`, `¿Adónde se ha ido?`).
  - Uses transitive `informar que` (`Me acaban de informar que...`) in accordance with educated Latin American usage rather than Peninsular `informar de que`.
- **Console & UI Terminology (First-Party `es-419` Standards):**
  - Action prompts use **`PRESIONA` / `PRESIONAR` / `MANTÉN PRESIONADO`** (aligned with Nintendo Switch, PlayStation, and Xbox LatAm standards) rather than Peninsular `PULSA` / `MANTÉN PULSADO`.
  - Hardware and media terms follow `es-419` conventions: **`CONTROL`** (not `mando`), **`COMPUTADORAS`** (not `ordenadores`), and **`LADO A / LADO B`** for vinyl/cassette sides (not `Cara A / Cara B`).
- **Lexical Neutrality:** Avoids country-specific idioms or Peninsularisms in dialogue (e.g., `misión de búsqueda` instead of Peninsular `misión de recadero`; `¡No lo puedo creer!` instead of Peninsular `¡No me lo puedo creer!`; `pájaro enojado` instead of `enfadado`).

#### 2. **Portuguese: Brazilian Portuguese (`pt-BR`) with Pan-Lusophone Care**
The Portuguese localization is written in **Brazilian Portuguese (`pt-BR`)**, while actively avoiding anatomical slang, scatological false friends, or Spanish calques so that players in any Lusophone country (Brazil, Portugal, Angola, Mozambique, Cabo Verde) can enjoy the game without unintended double meanings:
- **Pronouns, Syntax & Progressions:**
  - Uses **`você`** (not `tu`) and natural Brazilian progressive gerunds (`estou pensando`, `caminhando em sonhos`, `por ter voltado a cortar lenha`).
  - Uses natural Brazilian **proclisis** in character speech (`eu me sento`, `a tempestade se dissipou`, `onde uma mamãe pata se agitava`), while pairing first-person pronouns (`eu me sento`) or subordinate attractors so the syntax never reads awkwardly to other Lusophone readers.
  - Uses analytic past forms (`havia ouvido`, `tinha visto`) in narrative prose instead of stiff synthetic pluperfects (`ouvira`, `vira`).
- **Lexicon & Orthography:**
  - Follows PT-BR orthography and circumflex/acute accentuation (`Trígono`, `psicocosmologia mitopoética`, `fenômenos`) and standard Brazilian gaming/everyday vocabulary (`videogame`, `show de rock`, `controle`, `tela`, `cachoeira`, `cogumelo`, `legal`, `galera`).
- **Cross-Variant Semantic Safety (No *Portunholismos* or Unintended Innuendo):**
  - **No scatological or anatomical double meanings:** Uses **`operar milagres`** (never `obrar milagres`, which connotes defecation in Portuguese); **`estrela do rock em tempo integral`** (never `pau pra toda obra`, avoiding vulgar connotations of *pau* across the Lusophony); and **`Que desânimo!`** / **`é um fardo`** (instead of scrotal slang `Que saco!` / `é um saco`).
  - **No Spanish calques (*portunholismos*):** Uses idiomatic Portuguese expressions such as `estados de espírito` (not `estados de ânimo`), `sem parar` (not `uma e outra vez`), `Contra todas as probabilidades` (not `Contra ventos e marés`), `nos deixou meio irritados` (not `atravessados`), and `em breve ela desapareceria` (not `se iria`).

---

## Technical, UI & Engine Constraints (LQA Reference & Post-Mortem)

This section serves as an empirical **LQA post-mortem and technical changelog**. It documents strictly technical decisions—UI layout collisions, font atlas glyph registration, binary schema compatibility, TSV escaping, and cross-platform input behavior—backed by live in-engine testing across Nintendo Switch, PC (Steam), and iOS, alongside official internal developer notes from Capybara Games (`FIGS Notes` / `Craig's Notes` in `all-vo/strings.tsv` and `all-vo/dialog.tsv`).

### 1. `HOLD_SHIELD_TO_HEAL` (`strings.tsv` Line 127) — Deliberate Omission of "Shield"
- **Source (`en`)**: `HOLD SHIELD TO HEAL`
- **Spanish (`es-419`)**: `MANTÉN PARA CURARTE`
- **Portuguese (`pt-BR`)**: `SEGURE PARA SE CURAR`
- **Technical Evidence**:
  1. **Single-line non-wrapping HUD element**: In combat, the engine renders `HOLD_SHIELD_TO_HEAL` on a single horizontal line that **does not wrap** to a second row.
  2. **Sprite collision with the sword**: The text is centered directly over the glowing shield icon (`[ ▣ ]`) and sits immediately to the left of the vertical sword sprite (`|`). Even at 19–20 characters (`MANTÉN PARA CURARTE` / `SEGURE PARA SE CURAR`), the right end of the string sits just pixels away from the sword blade. Adding `"EL ESCUDO"` (`MANTÉN EL ESCUDO PARA CURARTE`, 29 chars) or `"O ESCUDO"` (`SEGURE O ESCUDO PARA SE CURAR`, 29 chars) causes the text to crash directly through the sword sprite.
  3. **Visual redundancy**: Because the label is anchored directly above the pulsing shield icon, the visual referent (*shield*) is self-evident to the player.

### 2. `QUIT` (`Line 99`), `SETTINGS` (`Line 133`), `GO_HOME` (`Line 29`) & `EXIT` (`Line 113`) — Slide-Out Tabs vs. Menu Hierarchy
- **`QUIT` (`strings.tsv` Line 99)**:
  - **Source (`en`)**: `QUIT?` (5 characters) | **Spanish (`es-419`)**: `SALIR` (5 characters) | **Portuguese (`pt-BR`)**: `SAIR?` (5 characters)
  - **Technical Evidence**:
    1. **Strict 5-character boundary in Capy's master sheet**: In `all-vo/strings.tsv` (Row 99), Capybara Games explicitly assigned a hard limit of **`Max characters: 5`**.
    2. **In-game sprite overlap**: The in-game pause exit prompt is rendered inside a narrow grey slide-out tab on the far-left edge of the screen terminated with an embedded circular button icon (`⊗`). When Spanish inverted question marks are added (`¿SALIR?`, 7 characters), the text exceeds the 5-character boundary and crashes directly through the circular icon (`¿SALI⊗?`). Omitting `¿...?` in Spanish (`SALIR`, 5 chars) fits cleanly within the boundary, while Portuguese `SAIR?` (5 chars, no opening `¿`) fits naturally.
- **`SETTINGS` (`strings.tsv` Line 133)**:
  - **Source (`en`)**: `SETTINGS` (8 characters) | **Spanish (`es-419`)**: `AJUSTES` (7 characters) | **Portuguese (`pt-BR`)**: `AJUSTES` (7 characters)
  - **Technical Evidence**: On the title screen, `SETTINGS` renders inside a fixed-width grey slide-out pill on the left edge with an embedded sliders icon (`[≡]`) on its right end (sized for the 8-character English word `SETTINGS`). Using `CONFIGURACIÓN` or `CONFIGURAÇÕES` (13 characters) crashes straight through the sliders icon and spills onto the background (`CONFIGURA[≡]ÓN` — a bug actually shipped in the official European `ES_FIGS` and `DE_FIGS` releases). `AJUSTES` (7 characters) fits inside the pill with zero collision.
- **Why `GO_HOME` (`strings.tsv` Line 29) allows 8 characters (`¿INICIO?` / `INÍCIO?`)**:
  - In `all-vo/strings.tsv` (Row 29), developer Matt Repetski (`MR`) explicitly noted: *"IT: What's the context/function of this string? MR - I think it's actually not being called, but in case we need it a literal translation would likely be fine"*, and the character limit column was set to `8`. `GO_HOME` is an **unreferenced prototype string** that never renders in the active in-game slide-out tab; hence its 8-character Spanish translation (`¿INICIO?`) does not collide with anything in-game.
- **Differentiating `QUIT` (Line 99) vs. `EXIT` (Line 113)**:
  - `QUIT` (`Line 99`) operates inside the in-game gameplay pause tab.
  - `EXIT` (`Line 113`, `Max characters: 4`) operates exclusively in the desktop PC display/graphics options screen (alongside `RESOLUTION`, `RESET`, `APPLY`, `BACK`).
  - Because `QUIT` and `EXIT` exist in completely distinct UI hierarchies and screens, using `SALIR` (ES) / `SAIR` (PT) for both mirrors standard OS conventions without creating any runtime collision or player ambiguity.

### 3. Sensitivity Controls: Motion, Analog Stick & Point-and-Click (`strings.tsv` Lines 130, 131, 177)
- **Strings**:
  - `MOTION_CURSOR_SENSITIVITY` (`Line 130`):
    - **Source (`en`)**: `MOTION CURSOR SENSITIVITY` | **Spanish (`es-419`)**: `SENSIBILIDAD: CURSOR POR MOVIMIENTO` | **Portuguese (`pt-BR`)**: `SENSIBILIDADE: CURSOR POR MOVIMENTO`
  - `STICK_CURSOR_SENSITIVITY` (`Line 131`):
    - **Source (`en`)**: `STICK CURSOR SENSITIVITY` | **Spanish (`es-419`)**: `SENSIBILIDAD: CURSOR ANALÓGICO` | **Portuguese (`pt-BR`)**: `SENSIBILIDADE: CURSOR ANALÓGICO`
  - `POINTCLICK_CURSORSENS_NINSWITCH` (`Line 177`):
    - **Source (`en`)**: `POINT & CLICK CURSOR SENSITIVITY` | **Spanish (`es-419`)**: `SENSIBILIDAD: APUNTAR Y HACER CLIC` | **Portuguese (`pt-BR`)**: `SENSIBILIDADE: APONTAR E CLICAR`
- **Technical & Design Evidence**:
  1. **Reinstatement of "Cursor" to Prevent Semantic Collision**: Earlier draft iterations translated these as `SENSIBILIDAD DE MOVIMIENTO` and `SENSIBILIDAD DEL JOYSTICK`, omitting "cursor". In Nintendo Switch menus, omitting "cursor" generated critical confusion between Joy-Con physical gyroscopic movement, character walking speed, and reticle aiming. Reinstating `CURSOR` guarantees players know which input layer is being tuned.
  2. **Menu Box Width Limits (35-character threshold on Switch)**:
     - On Nintendo Switch, the settings menu renders each option label immediately to the left of the sensitivity slider widget.
     - Translating `POINTCLICK_CURSORSENS_NINSWITCH` literally as `SENSIBILIDAD DEL CURSOR DE APUNTAR Y HACER CLIC` (45 characters) caused the text to overflow into the slider handle.
     - Standardizing all three sensitivity controls into the structured colon syntax **`SENSIBILIDAD: [MODO]`** (`SENSIBILIDADE: [MODO]`) cleanly differentiates the three control schemes while keeping all strings comfortably under 35 characters (`SENSIBILIDAD: APUNTAR Y HACER CLIC` = 34 chars).

### 4. `DIGIT_STRING` (Line 126) & `SPANISH_SPECIAL` (Line 167) — Bitmap Font Glyph Registration
- **`DIGIT_STRING` (`strings.tsv` Line 126)**:
  - **Source (`strings.en.tsv`)**: `123456789`
  - **Localized (`es-419` / `pt-BR`)**: `0123456789`
  - **Developer Evidence**: `strings.en.tsv` shows `123456789` only because spreadsheet auto-formatting stripped the leading `0` when the English column was exported from Excel. Capybara Games' official localization sheet (`FIGS Notes`, row 126) explicitly instructs localizers: *"This string used to automatically delete 0s at the beginning of the string because of formatting, so they must be re-added manually."* Removing `0` breaks character-set registration for the digit `0`.
- **`SPANISH_SPECIAL` (`strings.tsv` Line 167)**:
  - **Source (`strings.en.tsv`)**: `Á É Í Ó Ú Ñ Ü ¿ ¡ º ª « » ‹ › €` *(uppercase vowels/Ñ/Ü only)*
  - **Spanish (`es-419`)**: `Á á É é Í í Ó ó Ú ú Ñ ñ Ü ü ¿ ¡ º ª « » ‹ › €`
  - **Portuguese (`pt-BR`)**: `Á á Â â Ã ã À à Ç ç É é Ê ê Í í Ó ó Ô ô Õ õ Ú ú Ñ ñ Ü ü ¿ ¡ º ª « » ‹ › €`
  - **Technical Evidence**: Just like `DIGIT_STRING`, the `*_SPECIAL` rows declare special glyphs for bitmap font atlas/table registration. Because the official Switch source omitted lowercase Spanish vowels (`á é í ó ú ñ ü`) and did not contain Portuguese diacritics (`â ã à ç ê ô õ`), both files deliberately expand Row 167 to guarantee complete glyph coverage across all UI strings and dialogue boxes. Do not revert Row 167 to the truncated uppercase-only source string.

### 5. Multi-Platform `strings.tsv` Superset (236 Lines vs. 229 Lines in Switch `strings.en.tsv`) — Binary Schema & Key-Index Compatibility
- **Structure**: `strings.en.tsv` (from the Nintendo Switch release) contains **229 lines**, whereas `spanish/strings.tsv` and `portuguese/strings.tsv` contain **236 lines**.
- **Technical Evidence**:
  - Lines 1–229 match the Nintendo Switch `strings.en.tsv` 1-to-1 by key and row number.
  - Lines 230–236 are **7 legacy iOS and PC/Steam keys** stripped when Twitter integration and desktop exit dialogs were removed on Switch.
  - **Binary Schema Compatibility**: Retaining the full 236-key superset preserves lookup-table index compatibility across Nintendo Switch, PC (Steam), and legacy iOS/mobile binaries, allowing one unified `.tsv` per language to serve as a drop-in patch without missing-key runtime exceptions.
  - *(Empirical verification)*: Testing on vintage hardware (an iPod Touch running iOS 4 with the original 2011 Twitter-enabled build) confirmed that the mobile executable crashes immediately if any of these 7 keys are missing from `strings.tsv`.
- **Official English Source & MQM Audit Reference**:
  These 7 strings correspond directly to Capybara Games' historical English keys and are audited verbatim against the current localized files below:

| Row | Key / ID | Official Capybara Games English Source | Spanish (`es-419`) | Portuguese (`pt-BR`) | Context & Platform |
|:---:|---|---|---|---|---|
| **230** | `TWITTER_SELECT_BUTTON` | `SELECT` | `SELECCIONAR` | `SELECIONAR` | iOS Twitter account selection modal button |
| **231** | `TWITTER_SELECT_MSG` | `PLEASE SELECT A TWITTER ACCOUNT` | `"POR FAVOR, SELECCIONA UNA CUENTA DE TWITTER"` | `"POR FAVOR, SELECIONE UMA CONTA DO TWITTER"` | iOS Twitter dialog prompt |
| **232** | `TWITTER_NO_ACCOUNTS` | `There are no Twitter accounts configured on this device.` | `Configura Twitter en tu dispositivo` | `Configure o Twitter em seu dispositivo` | iOS system account check message |
| **233** | `TWITTER_REQUESTING` | `REQUESTING ACCESS...` | `SOLICITANDO ACCESO...` | `SOLICITANDO ACESSO...` | iOS OAuth/permission modal status |
| **234** | `TAP_QUESTION` | `TAP?` | `¿PRESIONAR?` | `PRESSIONAR?` | iOS/Mobile touch tutorial prompt |
| **235** | `EXIT_TITLE` | `Exit #sworcery?` | `¿Salir de #espadancia?` | `Sair de #espadancia?` | PC / Steam exit confirmation dialog title |
| **236** | `EXIT_PROMPT` | `Are you sure you want to exit?` | `¿En verdad quieres salir?` | `Você realmente deseja sair?` | PC / Steam exit confirmation dialog body |

### 6. `ARCHETYPE_TREEHINT` (`dialog.tsv` Line 230) — Cross-Platform Camera Mechanics (Mobile Touch vs. Desktop Edge-Hover & Keys)
- **Source Text Evolution**:
  - **Original iOS (2011)**: `Once you have begun to sing a song of sworcery you can ever-so-gently touch & swipe on the sworcery aura to look around.`
  - **PC / Steam (`dialog.en.tsv` Line 230, tagged `Old PC Version`)**: `Once you have begun a song of sworcery you can ever-so-gently touch the edge of the screen to look around (or use the arrow keys).`
  - **Nintendo Switch (`ARCHETYPE_TREEHINT_NINSWITCH`, Line 233)**: `Once you have begun a song of sworcery you may want to look around and take in your surroundings.` *(Developer note by Matt Repetski: "Switch will need its own most likely. Should cover moving camera with cursor, arrows/d-pad and also touch and drag...")*
- **Spanish (`es-419`)**: `Al entonar la Canción de Espadancia, desliza con suma suavidad el aura para mirar alrededor (o acerca el cursor al borde o usa las flechas).` (139 chars)
- **Portuguese (`pt-BR`)**: `Ao entoar a Canção da Espadância, deslize muito suavemente a aura para olhar ao redor (ou leve o cursor à borda da tela ou use as setas).` (139 chars)
- **Technical & Design Evidence**:
  1. **Unified Multi-Platform Deployment**: The exact same `dialog.tsv` table is compiled into both PC (Steam) and mobile (iOS & iPadOS) game distributions.
  2. **Total Breakdown of PC Instructions on Mobile (iOS / iPadOS)**:
     - On iOS/iPadOS, there is no mouse cursor to position at the edge of the screen.
     - Crucially, even when an external mouse, trackpad, or physical keyboard is paired to an iPad, the mobile engine's touch-input layer **does not process edge-of-screen cursor hovering or arrow keys for camera panning**.
     - On touch devices, **dragging the sworcery aura (*touch & swipe*) is the sole functional method** to pan the camera during a Song of Sworcery. Translating the English Steam string literally (*"touch the edge of the screen or use the arrow keys"*) completely misleads mobile players, as tapping/touching the screen edge does nothing.
  3. **Desktop Ambiguity & Imprecision on PC/Steam**:
     - The English PC phrasing (*"touch the edge of the screen"*) is itself technically imprecise on desktop: the player does not click or touch anything; the camera pans simply by **hovering / placing the cursor near the screen border**, or alternatively pressing the arrow keys.
     - Furthermore, the legacy touch mechanic—clicking and gently dragging the sworcery aura with the mouse cursor—**remains fully active and functional on PC**.
  4. **The Cross-Platform Editorial Bridge**:
     - To ensure complete functional clarity across iOS, iPadOS, and PC simultaneously, the localized strings make **aura swiping the primary universal instruction** (which works identically with a finger on mobile or with a mouse drag on PC), followed by a concise parenthetical covering desktop-specific controls (`(o acerca el cursor al borde o usa las flechas)` / `(ou leve o cursor à borda da tela ou use as setas)`). Both strings fit cleanly inside the 3-line dialogue box (ES/PT: 139 chars).

### 7. `ARCHETYPE_GROTTOPARADOX` (`dialog.tsv` Line 494) — Unreferenced Dead Code Row Parity
- **Source (`en`)**: `Once the moods of the moon have been altered in The Moon Grotto the`
- **Spanish (`es-419`)**: `Una vez que el humor de la luna ha sido alterado en la Gruta Lunar, la`
- **Portuguese (`pt-BR`)**: `Uma vez que o humor da lua foi alterado na Gruta Lunar, o`
- **Developer Evidence**: This line is truncated mid-sentence in the original English script. In `all-vo/dialog.tsv` (`FIGS Notes`, row 494), developer Matt Repetski confirmed: *"This is not actually being called, ignore it."* It is retained at Line 494 solely to preserve exact row parity across `dialog.tsv`.

### 8. Bitmap Font Glyph Limits & TSV Parser Escaping (`'...'` vs. `«...»` / `“...”`)
- **Rule**: Always use **single straight ASCII quotes (`'...'`)** for internal quotes, nicknames (`André 'El Gigante'`), UI prompts (`presiona 'Jugar'`), and cited words inside dialogue.
- **Technical Evidence**:
  1. **Bitmap font glyph limitations**: Although `SPANISH_SPECIAL` (Line 167) includes `« » ‹ ›` in the string table, the game's compiled bitmap fonts (`conduit_itc_2x.fnt`, `arial_narrow.fnt`) lack typographic curly quotes (`“ ” ‘ ’`) and single angle quotes (`‹ ›`).
  2. **TSV parser behavior**: Standard CSV/TSV cell quoting wraps fields containing commas or quotes in straight double quotes (`"..."`), escaping internal literal double quotes as `""`. Using single ASCII quotes `'...'` for inline citations avoids escaping errors and renders cleanly across all bitmap fonts.

### 9. Proportional Font Wrapping Heuristic (~140 chars), Hashtags, `S:S&SEP` & LIFO Dialogue Stack
- **Proportional Bitmap Font Wrapping (~140 chars heuristic)**:
  - Because `conduit_itc_2x.fnt` and `arial_narrow.fnt` are **proportional bitmap fonts** (not monospaced), actual line breaks in the 3-line tweet box depend on cumulative pixel width rather than raw character count—a 136-character string rich in wide uppercase glyphs (`M`, `W`, `G`) can wrap onto a 4th line earlier than a 142-character string rich in narrow glyphs (`i`, `l`, spaces).
  - Keeping playable lines under **~140 characters total** (~42–46 per row) is therefore documented as an empirical **safe length heuristic** always subject to in-game visual verification, not a deterministic character-count guarantee.
- **Unaccented Hashtags**: Acute accents and tilde diacritics on vowels are intentionally omitted inside hashtags (`#si`, `#quizas`, `#trigondomado`, `#masfacildelopensado`, `#olamundo`, `#nao`, `#matanca`) to reflect authentic 2011 Twitter parsing behavior, while `ñ` is preserved in Spanish (`#leñando`, `#bañomutante`).
- **Unified `S:S&SEP` Acronym**: While `dialog.en.tsv` inconsistently mixes `S:S&SEP` and `S:S&S EP`, ES/PT standardize the compact form **`S:S&SEP`** across all UI and dialogue boxes to save horizontal pixel width and ensure consistency.
- **LIFO (Bottom-to-Top) Dialogue Stack**: Several multi-line blocks (`ARCHETYPE_FOUNDATION` `D056–D067`, `GCLUE_*`, `ARCHETYPE_*TRIGONCOLLECTED` `D486–D488`) are pushed onto an engine stack and displayed **from bottom to top** (e.g., `D066 → D065 → D064 → D063 → D062`). Always verify pronoun antecedents in actual in-game reading order rather than top-to-bottom TSV row order.

---

## Editorial Deviations & Transcreation Rationale

Unlike §10, the entries below are **purely linguistic, narrative, and stylistic editorial decisions**—not technical limitations of the game engine. They are documented transparently here for LQA reviewers and MQM auditors:

### 1. `SCYTHIAN_FOUNDATION` (`dialog.tsv` Line 508) — Narrative Slip Correction (`singular / plural`)
- **Source (`en`)**: `Wait... why am I referring to myself in first person? I thought our story was told in second person? #editingoversight`
- **Spanish (`es-419`)**: `Espera... ¿por qué hablo en singular? ¿No se supone que la historia va en plural? #erratadeedicion`
- **Portuguese (`pt-BR`)**: `Espera... por que estou falando no singular? Não era para a história ser no plural? #erratadeedicao`
- **Editorial Evidence**: In the English script, the writer accidentally confused *"first-person plural"* (*we / our*) with *"second person"* (*you*). Throughout the game, The Scythian narrates in the **first-person plural** (*we* / *nosotros* / *nós*), and in `D508–D510` she momentarily slips into the **first-person singular** (*I / my*). Translating literally (`primera persona / segunda persona`) breaks the meta-joke because `"nuestra historia"` is first-person plural, not second person. Contrasting **`en singular` / `en plural`** (`no singular` / `no plural`)—just as the official 8-4 Japanese localization did—restores the intended fourth-wall joke.

### 2. Direct-Speech Explicitación in Ghost Telepathic Transmissions (`D145–D146`, `D150–D151`, `D156–D167`, `D170–D178`, `D531`)
- **Pattern**: The Spanish and Portuguese localizations add literal double quotation marks (`"""..."""`) to dialogue blocks spoken by ghosts/spirits (e.g., `D145`, `D150`, `D156`, `D170`) and Samae's dream (`D531`), where the English script displays **no rendered quotation marks**.
- **Lore & Editorial Rationale**:
  - In the English original, dialogue from living characters (`Logfella`, `Samae`) does **not** carry rendered quotation marks either (`D531` in `dialog.en.tsv` has only outer CSV field quotes due to an internal comma; literal quotes in English appear only on carved signs `D004–D005` and selected Archetype transmissions `D068–D071`, `D081–D086`).
  - Within the game's lore (`D067`, `D069`) and credits (`D594–D596`), only The Scythian, Logfella, and The Archetype have vocal performances; ghosts project silent telepathic *"linguistic thought-transmissions"* intercepted via The Megatome.
  - Adding literal double quotes in Spanish and Portuguese is therefore **not correcting a Capybara Games typo**—it is an **intentional stylistic explicitación** for Romance readers, ensuring immediate visual clarity when a ghost's first-person voice (`I` → `yo` / `eu`) alternates within the same scene against The Scythian's surrounding first-person plural narration (`nosotros` / `nós`). This addition has zero effect on engine behavior.

### 3. `ARCHETYPE_GOLDMASTERINTRO` (`dialog.tsv` Line 283) — Creative Cultural License & Register Shift
- **Source (`en`)**: `Confused? Excellent. Keep calm & carry on.`
- **Spanish (`es-419`)**: `¿Confusión? Calma, calma, ¡que no panda el cúnico!`
- **Portuguese (`pt-BR`)**: `Confusão? Palma, palma, não priemos cânico!`
- **Editorial Note on Character Voice**:
  - Under *Character Voice & Tone*, The Archetype is normally defined as *"The Erudite Guide"* with a formal, academic register. This line is an **explicitly acknowledged creative license and register break**:
  - Just as the English script momentarily pivots away from arcane psychocosmology into a ubiquitous British cultural meme (*"Keep calm & carry on"*), the Spanish and Portuguese localizations prioritize immediate pan-Latin American / Brazilian pop-culture levity by substituting Roberto Gómez Bolaños's (*El Chapulín Colorado* / *Chapolin Colorado*) iconic catchphrase, accepting the playful break in character solemnity for fourth-wall comedic impact.

---

## Cultural References, Pop-Culture Homages & Literary Allusions (Cross-Language Guide)

*Superbrothers: Sword & Sworcery EP* blends Iron Age Scythian myth with dense layers of cinema, indie music, comic-book, videogame, and countercultural allusions. This reference table catalogs every cultural wink in `dialog.tsv` so translators porting the game into additional languages can identify the underlying homage and adapt it faithfully.

### 1. Cinema & Television

| Row & ID | English Source | Cultural Reference & Context | Spanish (`es-419`) & Portuguese (`pt-BR`) Adaptation | Advice for Other Languages |
|---|---|---|---|---|
| `D103` (`INFO_WELLWHITESTAG`) | `LONG LIVE THE NEW FLESH` | **David Cronenberg's *Videodrome* (1983):** Max Renn's final mantra before transcending his physical body. | **ES:** `LARGA VIDA A LA NUEVA CARNE`<br>**PT:** `VIDA LONGA À NOVA CARNE` | Use the official localized dub/subtitle quote from *Videodrome* in your target language. |
| `D108` (`INFO_NESTBOX`) | `We spied a curious-looking nestbox, now home to a wretched hive.` | ***Star Wars: Episode IV – A New Hope* (1977):** Obi-Wan Kenobi describing Mos Eisley (*"You will never find a more wretched hive of scum and villainy"*), playing on a literal wasp/bee *hive* inside the birdhouse. | **ES:** `... ahora era hogar de una colmena de escoria y villanía.`<br>**PT:** `... agora lar de uma colmeia de escória e vilania.` | Echo the canonical *Star Wars* phrasing for *"hive of scum and villainy"* so the pun on a literal insect hive is unmistakable. |
| `D132` (`INFO_ROCKSHOWGIRL`) | `At a rock show we spied Samae & we thought maybe she said fire walk with me.` | **David Lynch's *Twin Peaks* (1990–1992):** The iconic poem (*"Fire, walk with me"*) and prequel film *Twin Peaks: Fire Walk with Me*. | **ES:** `... 'Fuego, camina conmigo'.`<br>**PT:** `... 'Fogo, caminha comigo'.` | Preserve the exact canonical *Twin Peaks* phrasing in your language, even if its imperative pronoun form differs from the rest of the script. |
| `D375–D376` (`GCLUE_LAKESHORELAKE`) | `My logs have many secrets... Unfortunately I don't speak log-language.` / `In my experience there are times when owls are not what they seem...` | **David Lynch's *Twin Peaks* (The Log Lady & The Giant):** A double homage in the same LIFO dialogue block. First (`D376`), Logfella echoes The Giant's warning to Agent Cooper (*"The owls are not what they seem"*); second (`D375`), Logfella—who, like Margaret Lanterman (**The Log Lady**), carries a log in his arms everywhere—parodies her famous introductions (*"My log has something to tell you"* / *"My log saw something"*), joking that his logs hold secrets too, except he doesn't speak `"log-language"`. | **ES:** `... no hablo tronqués.` / `... a veces los búhos no son lo que parecen...`<br>**PT:** `... não falo tronquês.` / `... às vezes as corujas não são o que parecem...` | Coin a playful language name from the word for *log* (`tronco` + `-és`/`-ês` → `tronqués`/`tronquês`) in `D375`, and match the canonical *Twin Peaks* owl quote in `D376`. |
| `D558–D560` (`LOGFELLA_CRESCENTWANE`) | `...from whence The Megatome had come in a distant Stone Age. He spoke of immortals from space who sparked in mankind...` | **Arthur C. Clarke & Stanley Kubrick's *2001: A Space Odyssey* (1968):** The extraterrestrial Monolith arriving in the Stone Age ("The Dawn of Man") to spark human intelligence. | Translated with solemn, mythic-scientific phrasing in both ES and PT. | Keep the solemn, cosmic-horror register of Clarke's Monolith mythos. |

### 2. Music, Street Art & Comics

| Row & ID | English Source | Cultural Reference & Context | Spanish (`es-419`) & Portuguese (`pt-BR`) Adaptation | Advice for Other Languages |
|---|---|---|---|---|
| `D004` (`SIGN_TADPOL`) | `"""Home is where the hearth is."" #threegutrecords4ever"` | **Three Gut Records:** The influential Canadian independent record label co-founded by composer Jim Guthrie in Guelph/Toronto (1999–2005). Also a pun on *"Home is where the heart is"* vs. *"hearth"* (fireplace). | **ES:** `"""Donde el fuego alumbra, el hogar se vislumbra."" #threegutrecordsx100pre"`<br>**PT:** `"""Onde a lareira arde, o lar faz alarde."" #threegutrecordsprasempre"` | Keep `threegutrecords` intact in the hashtag and recreate the *heart/hearth* wordplay with a warm proverb or rhyme about fire (`fuego`/`lareira`) and home (`hogar`/`lar`). |
| `D035`, `D321` | `...to move it move it move it.` / `...to move it move it extra fast...` | **Reel 2 Real feat. The Mad Stuntman – *"I Like to Move It"* (1993):** Eurodance classic popularized globally by King Julien in DreamWorks' *Madagascar* (2005). | **ES:** `¡y a mover, mover el bote!` / `mover el bote`<br>**PT:** `nos remexer, remexer, remexer!` / `se remexer` | Use the recognizable localized hook from the *Madagascar* dub in your language (`mover el bote` in LatAm Spanish; `eu me remexo muito` in Brazilian Portuguese). |
| `D127` (`INFO_CABINRECORD`) | `...above the hearth. #theballadofthespacebabies` | ***"The Ballad of the Space Babies"*:** Flagship track on Jim Guthrie's *Sword & Sworcery LP: The Ballad of the Space Babies* soundtrack. | Kept as `#theballadofthespacebabies` in ES and PT. | Leave the song title hashtag in English so it links directly to the official track title. |
| `D170` (`GRAVE_MEADOWGHOST*`) | `Last year before the yuletide Andre The Giant assembled a posse...` | **André the Giant & Shepard Fairey's *"Andre the Giant Has a Posse"* (1989):** Dual nod to legendary wrestler/actor André the Giant (*The Princess Bride*) and Shepard Fairey's street-art sticker campaign (*OBEY*). | **ES:** `André 'El Gigante' juntó a su gente...`<br>**PT:** `André, 'O Gigante', juntou a galera...` | Translate the epithet (`The Giant`) while keeping `André` recognizable. |
| `D250`, `D418` (`ARCHETYPE_MEADOWHINT`, `MIRACLE1_MOUNTAINMEADOW`) | `...the miraculous fold-in abilities of the great wizard Al Jaffee.` / `...in the fold-in fashion of the mad wizard Al Jaffee.` | **Al Jaffee (1921–2023) & *MAD Magazine* Fold-Ins:** Jaffee created the back-cover *MAD Fold-In*, where folding the page inward brings two distant edges together to form a new image—the exact gameplay mechanic of the Meadow Miracle. | **ES:** `los milagrosos poderes de plegado del gran mago Al Jaffee`<br>**PT:** `os milagrosos poderes de dobra do grande mago Al Jaffee` | Keep **Al Jaffee** untouched and use the word for *folding* a page (`plegado` / `dobra`) so the visual puzzle hint remains clear. |
| `D355` (`GCLUE_MOUNTAINMEADOW`) | `...a dog's gotta do what a dog's gotta do what a dog's gotta do do.` | **Turntable record-skip / sample loop + *"do-do"* (poop) pun:** Parodies the western cliché *"A man's gotta do what a man's gotta do"* while stuttering like a vinyl record or hip-hop scratch (`do-do`). | **ES:** `... lo que un perro tiene que ha-ha-hacer.`<br>**PT:** `... o que um cão tem que fa-fa-fazer.` | Recreate the rhythmic vinyl-stutter at the end of the repeated verb. |
| `D404`, `D405` (`JIM_LOGFELLATHOUGHTS`) | `#1000songs` / `#andwegotolder` | **Jim Guthrie's discography:** References his *1000 Songs* project and his indie track *"And We Got Older"* (from *Now, More Than Ever*, 2003). | Kept as `#1000songs` and `#andwegotolder`. | Keep the English song/project hashtags intact as musical Easter eggs. |
| `D412` (`LOGFELLA_MOONGROTTOCOMMENT`) | `It's a long way from 0 to 1 & if an alien said hello it'd be in cryptic code on the stereo. Wait... what?` | **Jim Guthrie – *"Hands in My Pocket"* (*Now, More Than Ever*, 2003) & Moon Grotto SSTV/audio cipher:** Paraphrases Guthrie's lyrics while hinting at the hidden audio transmission in the Moon Grotto. | **ES:** `Del 0 al 1 hay un largo trecho, y si un alien nos dijera 'hola', sería mediante un código críptico por el estéreo. Espera... ¿qué?`<br>**PT:** `Do 0 ao 1 há um longo caminho, e se um alien nos dissesse 'olá', seria em código críptico no estéreo. Pera... o quê?` | Preserve the internal rhyme or cadence (`hello / stereo`, `0 to 1`) and the confused `Wait... what?` punchline. |

### 3. Videogames & Tech Culture

| Row & ID | English Source | Cultural Reference & Context | Spanish (`es-419`) & Portuguese (`pt-BR`) Adaptation | Advice for Other Languages |
|---|---|---|---|---|
| `D002` (`GIRL_TONGUES`) | `...in a sunlit meadow. #helloworld` | **`"Hello, World!"`:** The canonical first string printed when learning a programming language or booting a new system (used on the very first line of the game). | **ES:** `#holamundo`<br>**PT:** `#olamundo` | Use the standard programming `"Hello, World!"` equivalent in your language. |
| `D006`, `D038` (`SIGN_CHASM`, `LOGFELLA_PRECIPICE_DONE`) | `...a stone carved with the glyph of a skyward sword...` / `...the nearby glyph depicting the skyward sword.` | ***The Legend of Zelda: Skyward Sword* (unveiled at E3 June 2010):** Nintendo revealed *Skyward Sword* (and Link's signature gesture of raising his sword skyward to charge a beam) while *S:S&SEP* was in full production in 2010; the Scythian's own sword-raising mechanic and this phrasing are a direct contemporary nod. | **ES:** `... una espada alzada al cielo...`<br>**PT:** `... uma espada apontada ao céu...` | Since *Skyward Sword* was never officially translated in Nintendo's localized game titles, render the image naturally and poetically (`espada alzada al cielo` / `espada apontada ao céu`). |
| `D089`, `D098`, `D251` (`INFO_BIRDEYESCULPTURE`, `ARCHETYPE_MEADOWHINT`) | `We spied an angry bird sculpture looming above the meadow. #subtlereference` | **Rovio's *Angry Birds* (2009):** A self-aware wink (`#subtlereference`) to the dominant iOS App Store hit at the time of *S:S&SEP*'s 2011 iPad/iPhone debut. | **ES:** `... un pájaro enojado... #sutilreferencia`<br>**PT:** `... um pássaro zangado... #sutilreferencia` | Translate literally (`angry bird`) so it describes the scowling stone bird statues while keeping the wink obvious. |
| `D308`, `D311–D319` | `...upload The Megatome to the whirling infinite atop Mingi Taw.` | **Cloud Computing (`upload` to *The Kingdom of the Cloud*):** Earlier in `D005`, Mingi Taw is called *The Kingdom of the Cloud*. "Uploading" the Megatome to the summit is a deliberate tech-anachronism punning on uploading data to "the Cloud." | **ES:** `subir el Megatomo` / `subimos el Megatomo`<br>**PT:** `subir o Megatomo` / `subimos o Megatomo` | Use the modern digital verb for *uploading to the cloud* (`subir`) rather than a physical verb like "carry" so the Cloud pun lands. |
| `D675` (`CREDITS`) | `S:S&S EP is a link to the past.` | ***The Legend of Zelda: A Link to the Past* (SNES, 1991):** One of the game's primary design inspirations, playing on the double meaning of *link* (connection vs. Nintendo's hero Link). | **ES:** `S:S&SEP es un 'Link' al pasado.`<br>**PT:** `S:S&SEP é um 'Link' com o passado.` | Capitalizing `'Link'` in single quotes preserves the *Zelda* tribute in languages where the noun for "connection" wouldn't otherwise evoke the character Link. |
| `D683` (`CREDITS`) | `S:S&S EP was originally going to be called 'Poopsock'. This is actually true.` | **`"Poopsock"` (MMORPG slang):** Early-2000s gaming slang for playing a game so obsessively that one refuses to leave the computer even to use the bathroom. | **ES:** `S:S&SEP iba a llamarse 'Poopsock' originalmente. Esto es totalmente cierto.`<br>**PT:** `S:S&SEP ia se chamar 'Poopsock' originalmente. Isso é totalmente verdade.` | Keep `'Poopsock'` untranslated as the historical working title. |

### 4. Literature, Philosophy, Politics & Folklore

| Row & ID | English Source | Cultural Reference & Context | Spanish (`es-419`) & Portuguese (`pt-BR`) Adaptation | Advice for Other Languages |
|---|---|---|---|---|
| `D101–D102` (`INFO_UNWELLWELL`, `INFO_WELLNESS`) | `The well seemed unwell. #unwell #well` / `All's well that ends well. #unwell #well #wellness` | **William Shakespeare's *All's Well That Ends Well* (c. 1604):** Preceded by a homophonic pun on *well* (water well) and *unwell* (sick). | **ES:** `El pozo soltó un sollozo. #pozo #sollozo` / `Bien está lo que bien acaba.`<br>**PT:** `O poço soltou um soluço. #poco #soluco` / `Bem está o que bem acaba.` | Since the water-well/good-health homophony rarely exists in other languages, use sonic rhyme (`pozo/sollozo`, `poço/soluço`) in `D101` and the canonical Shakespearean proverb in `D102`. |
| `D234` (`ARCHETYPE_MUSHROOMHINT`) | `It has even been asserted that divinatory mushrooms may have played a significant role in the development of the human psyche.` | **Terence McKenna's *"Stoned Ape" Hypothesis* (*Food of the Gods*, 1992):** The countercultural theory that psilocybin mushrooms catalyzed human language and self-reflection. | **ES:** `Incluso se ha postulado que los hongos adivinatorios pudieron haber tenido un papel clave en el desarrollo de la psique humana.`<br>**PT:** `Chegou-se a afirmar que os cogumelos adivinhatórios podem ter desempenhado um papel significativo no desenvolvimento da psique humana.` | Maintain the pseudo-academic, tentative register (`It has even been asserted... may have played`). |
| `D283` (`ARCHETYPE_GOLDMASTERINTRO`) | `Confused? Excellent. Keep calm & carry on.` | **1939 British Wartime Poster (*"Keep Calm and Carry On"*) → Adapted to *El Chapulín Colorado*:** The ubiquitous British motivational slogan, transcreated into Roberto Gómez Bolaños's beloved spoonerism. | **ES:** `¿Confusión? Calma, calma, ¡que no panda el cúnico!`<br>**PT:** `Confusão? Palma, palma, não priemos cânico!` | Either reference the *Keep Calm* slogan or adapt with an equally iconic, good-natured comedic catchphrase about staying calm in your target culture. |
| `D372–D373`, `D383` (`GCLUE_*`) | `There are two types of unknowns - the known unknowns & the unknown unknowns.` / `There are also unknown nouns...` | **Donald Rumsfeld's February 12, 2002 Pentagon Briefing:** Famous epistemological tongue-twister about *"known unknowns"* and *"unknown unknowns"*, followed by a pun on *unknowns / unknown nouns*. | **ES:** `Hay dos tipos de incógnitas: las incógnitas conocidas y las incógnitas desconocidas.`<br>**PT:** `Há dois tipos de incógnitas: as incógnitas conhecidas e as incógnitas desconhecidas.` | Use the recognized philosophical/political translation of Rumsfeld's *"known unknowns"* in your language. |
| `D599` (`CREDITS`) | `Executive producer, hero of the people, leadership & strategery by Nathan Vella...` | **`"Strategery"` (*Saturday Night Live*, 2000):** Mock-presidential malapropism coined by Will Ferrell impersonating George W. Bush in a 2000 *SNL* debate sketch. | **ES:** `... liderazgo y estrategeria...`<br>**PT:** `... liderança e estrategueria...` | Coin a playful portmanteau on *strategy* (`estrategia` → `estrategeria`) to preserve the humorous neologism. |
| `D674` (`CREDITS`) | `...the mythopoetic psychocosmology of Robert E. Howard's sword and sorcery stories...` | **Robert E. Howard (1906–1936):** Pulp-fantasy pioneer who created *Conan the Cimmerian* and founded the *Sword and Sorcery* genre (whose prehistoric Hyborian Age draws directly on historical Cimmeria and Scythia). | **ES:** `... las historias de espada y hechicería de Robert E. Howard.`<br>**PT:** `... as histórias de espada e feitiçaria de Robert E. Howard.` | Use the established literary name of the *Sword & Sorcery* subgenre in your language (`espada y hechicería` / `espada e feitiçaria`). |
| `D678` (`CREDITS`) | `S:S&S EP obliquely references Carl G. Jung & his fascinating ""Red Book"" all over the damn place.` | **Carl G. Jung's *The Red Book* (*Liber Novus*, published 2009):** Jung's illuminated manuscript of active imagination, archetypes, and dream-walking, which directly inspired **The Archetype** and the crimson **Megatome**. | **ES:** `... Carl G. Jung y su fascinante 'Libro Rojo'...`<br>**PT:** `... Carl G. Jung e seu fascinante 'Livro Vermelho'...` | Use the published title of Jung's *Liber Novus* (`El Libro Rojo` / `O Livro Vermelho`) in your language. |

---

## Quick Reference: Most Common Terms

### Top 20 Critical Terms

| # | English | Spanish | Portuguese |
|---|---------|---------|------------|
| 1 | The Scythian | La Escita | A Citiana |
| 2 | Sworcery | Espadancia | Espadância |
| 3 | The Megatome | El Megatomo | O Megatomo |
| 4 | sylvan sprite | espíritu silvano | espírito silvano |
| 5 | The Bright Moon looms | La Luna Radiante impera | A Lua Radiante paira |
| 6 | The Dark Moon reigns | La Luna Sombría reina | A Lua Sombria reina |
| 7 | woeful errand | funesto cometido | funesta missão |
| 8 | Logfella | Tronquero | Troncadeiro |
| 9 | Mingi Taw | Mingi Taw | Mingi Taw |
| 10 | The Gogolithic Mass | La Masa Gogolítica | A Massa Gogolítica |
| 11 | Trigon Trifecta | Tríada Trigónica | Tríade Trigônica |
| 12 | sonorous spume | susurrantes espumas | sussurrantes espumas |
| 13 | dream-walking | paseos oníricos / caminar en sueños | caminhadas oníricas / caminhar em sonhos |
| 14 | the whirling infinite | Arremolinado Infinito | Remoinhado Infinito |
| 15 | press & hold / touch & hold | mantén presionado | mantenha pressionado / segure |
| 16 | Perilous Precipice | Precipicio Peligroso | Precipício Perigoso |
| 17 | old road | antiguo camino | antigo caminho |
| 18 | stone hut | choza de piedra | cabana de pedra |
| 19 | deepwater pond | insondable estanque | insondável lagoa |
| 20 | heebie jeebies | los pelos de punta | frio na espinha |

---

## Appendix: Translation Philosophy

### Approach
These translations prioritize:
1. **Poetic/epic tone** appropriate to sword & sorcery genre
2. **Cultural adaptation** over literal translation
3. **Consistency** in terminology across entire game
4. **Playability** - terms must be clear in gameplay context

### Neologism Strategy
- "Sworcery" required creative solution in both languages.
- **Style Rule:** Treated as a common noun (lowercase) in both languages, similar to "magic" or "science", except when used in the proper title "Song of Sworcery" or when first introduced/defined.
- **Spanish: "espadancia"**. The `-ancia` suffix (like `constancia`, `elegancia`) gives it a more abstract, psionic, and philosophical quality, reflecting the game's description of it as a "consciousness expansion technique" rather than a standard form of magic.
- **Portuguese: "espadância"**. A brilliant neologism using the `-ância` suffix to create a similar mystical and unique feel.

### Character Names
- **Logfella**: Wordplay on "fella" + wood/logs
  - **Spanish: "Tronquero"**. "Tronquero" (`Tronco` + `-ero`) creates a rustic, descriptive nickname that reflects the character's profession. It mirrors the spirit of the original and the creativity of the Portuguese version, sounding like an authentic apodo de pueblo.
  - **Portuguese: "Troncadeiro"**. A creative and effective neologism for "the one who deals with logs".
- **Dogfella**: Parallel construction
  - **Spanish: "Perrero"**. Creates a perfect parallel to "Tronquero" using the same `-ero` suffix. While "perrero" can have other meanings, in the context of a rustic nickname, it clearly means "the dog guy" or "the one with the dog," which fits perfectly. It is more universal and sonically stronger than regional alternatives like "Chuchero".
  - **Portuguese: "Cachorreiro"**. Follows the same parallel structure as "Troncadeiro".

---

## Version History

- **v1.0** (2024) - Initial glossary creation
- **v1.1** (2024) - Added post-correction standards
- **v1.2** (2024) - Added grammar guidelines and critical error fixes
- **v1.3** (2026) - Harmonized cross-lingual standards between ES-419 and PT-BR and purged obsolete prototype rules following comprehensive in-game review
- **v1.4** (2026) - Added Technical, UI & Engine Constraints (LQA Reference) documenting in-game HUD collisions (`HOLD_SHIELD_TO_HEAL`, `QUIT`), `DIGIT_STRING`, multi-platform key superset, `ARCHETYPE_TREEHINT` cross-platform camera mechanics, `ARCHETYPE_GROTTOPARADOX`, `SCYTHIAN_FOUNDATION`, and bitmap font quote rules
- **v1.5** (2026) - Added comprehensive Cross-Language Guide of Cultural References, Pop-Culture Homages & Literary Allusions (`Twin Peaks`, `Videodrome`, `Star Wars`, `2001: A Space Odyssey`, `MAD Magazine / Al Jaffee`, `Shepard Fairey / Andre the Giant`, `Three Gut Records`, `Jim Guthrie`, `Zelda: A Link to the Past`, `Angry Birds`, `Shakespeare`, `Terence McKenna`, `Donald Rumsfeld`, `SNL / Strategery`, `El Chapulín Colorado`, `Robert E. Howard`, and `Carl Jung's Red Book`)
- **v1.6** (2026) - Addressed formal LQA/MQM audit feedback: added official Capybara Games English source table for rows 230–236 in `strings.tsv` with retro-hardware backward compatibility justification (iOS 4 / iPod Touch), documented sensitivity controls taxonomy (`MOTION_CURSOR_SENSITIVITY`, `STICK_CURSOR_SENSITIVITY`, `POINTCLICK_CURSORSENS_NINSWITCH`), clarified `GO_HOME` dead-code vs. `QUIT`/`EXIT` UI hierarchies, resolved engine quote parser distinction with ghost direct-speech normalization, and articulated the two-tier architecture of the document (§1–§9 Normative Style Guide vs. §10 Technical LQA Post-Mortem)
- **v1.7** (2026) - Resolved v1.6 LQA audit discrepancies: synchronized rows 232 & 234 (`TAP_QUESTION` → `¿PRESIONAR?` / `PRESSIONAR?`) with actual `.tsv` files, documented `SPANISH_SPECIAL` glyph registration (Row 167), separated pure technical engine constraints (§10) from creative/editorial decisions (§11 *Editorial Deviations & Transcreation Rationale*), deduplicated HUD rules in §4/§7/§9, reformulated ~140-char guidance as a proportional-font pixel heuristic, refined rows 230–236 rationale to binary schema compatibility, corrected telepathic ghost-quote lore facts, and explicitly documented `D283` as a creative character-voice license

---

## Contributors & Acknowledgments

- **Original game text:** Superbrothers Inc., Capy Games, Jim Guthrie
- **Spanish & Portuguese localizations:** [cesardeg](https://github.com/cesardeg)

For questions, corrections, or additions to this glossary, please submit issues to the repository.

---

## License

This translation glossary is provided as reference documentation for the Superbrothers: Sword & Sworcery EP localization project. Usage rights follow the game's original licensing terms.