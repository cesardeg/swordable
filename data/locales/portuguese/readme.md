# Translation Glossary & Style Guide: Sword & Sworcery EP — Portuguese (`pt-BR`)

> **Global Reference:** This guide covers **Brazilian Portuguese (`pt-BR`)** terminology, grammar, dialect standards, and localization decisions for [`dialog.tsv`](dialog.tsv) and [`strings.tsv`](strings.tsv). For engine-wide technical constraints, universal translation philosophy, base character archetypes, and the full cross-language cultural allusions guide, see the **[Global Localization Guide](../readme.md)**.

---

## Purpose & Scope

This document serves as the **authoritative Portuguese (`pt-BR`) reference** for *Superbrothers: Sword & Sworcery EP*. It pairs with the [Global Localization Guide](../readme.md) and documents:

1. **Normative Portuguese Master Glossary (§1–§8):** Canonical terminology for characters, locations, items, gameplay mechanics, lore, moon cycles, UI/system labels, and idioms.
2. **Grammar, Voice & Dialect Standards (§9–§11):** Portuguese-specific style rules, character voice nuances, and Brazilian Portuguese (`pt-BR`) pan-Lusophone conventions.
3. **Portuguese Technical Implementations, Editorial Decisions & Cultural Adaptations (§12–§14):** Concrete Portuguese implementations of engine/UI constraints, deliberate transcreation rationales, and pop-culture adaptations.

### Target Audience
- Portuguese translators, editors, and QA testers
- LQA/MQM auditors evaluating linguistic compliance and technical playability
- Community contributors, modders, and documentation writers

### Usage Guidelines
- **Mandatory terms** are marked with ✅ and must be used exactly as specified
- **Context-dependent** terms are marked with ⚠️ and include usage notes
- **Creative alternatives** are provided where multiple valid options exist
- All terms reflect **post-correction standards** verified against [`portuguese/dialog.tsv`](dialog.tsv), [`portuguese/strings.tsv`](strings.tsv), and in-game builds

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
9. [Grammar & Style Guidelines (`pt-BR`)](#grammar--style-guidelines-pt-br)
10. [Character Voice & Tone (Portuguese Nuances)](#character-voice--tone-portuguese-nuances)
11. [Dialect & Regional Standards (`pt-BR`)](#dialect--regional-standards-pt-br)
12. [Portuguese Technical Implementations & LQA Reference](#portuguese-technical-implementations--lqa-reference)
13. [Editorial Deviations & Transcreation Rationale (`pt-BR`)](#editorial-deviations--transcreation-rationale-pt-br)
14. [Cultural Adaptations (`pt-BR`)](#cultural-adaptations-pt-br)
15. [Quick Reference: Top 20 Critical Terms](#quick-reference-top-20-critical-terms)
16. [Portuguese Translation Philosophy](#portuguese-translation-philosophy)
17. [Version History](#version-history)
18. [Contributors & License](#contributors--license)

---

## Characters & NPCs

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **The Scythian (heroine)** | A Citiana | ✅ Player character. `"A Citiana"` is preserved to avoid homophonic clash with *cita/citar*. |
| **Scythians (demonym / tribe)** | os citas / cita | ✅ Demonym for the Scythian people. Regularized to `"citas / cita"`. |
| **Logfella** | Troncadeiro | ✅ The woodcutter. See [Portuguese Translation Philosophy](#portuguese-translation-philosophy). |
| **Girl / Samae** | Samae | ✅ Always `"Samae"` after introduction |
| | A garota de cabelos escuros | First appearance description |
| **The Archetype** | O Arquétipo | ✅ The guide character (contracts as `do Arquétipo` after prepositions) |
| **Dogfella** | Cachorreiro | ✅ The dog. See [Portuguese Translation Philosophy](#portuguese-translation-philosophy). |
| **Jim Guthrie** | Jim Guthrie | ✅ Never translate proper name |
| **The Grizzled Boor** | O Patife Grisalho | ✅ Antagonist (appears as `o Patife Grisalho` in running prose) |
| **Andre (The Giant)** | André, 'O Gigante' | ✅ Ghost character, maintain single quotes |
| **The Gogolithic Mass** | a Massa Gogolítica | ✅ The deathless specter (lowercase article in running prose) |

---

## Locations & Places

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **Mingi Taw** | Mingi Taw | ✅ Main mountain |
| **The Caucasus** | o Cáucaso | ✅ Geographic region |
| **Scythia** | Cítia | ✅ Homeland region |
| **The Perilous Precipice** | o Precipício Perigoso | ✅ Major location |
| **Trigon Grove** | Clareira Trigônica | ✅ Grove clearing |
| **The Moon Grotto** | a Gruta Lunar | ✅ Secret location |
| **The Kingdom of the Cloud** | o Reino da Nuvem | ✅ Mingi Taw's title |
| | | |
| **stone hut** | cabana de pedra | ⚠️ Logfella's dwelling |
| **stone wall** | muro de pedra | ✅ Blocks the old road |
| **meadow** | campina | ✅ Starting area |
| **deepwater pond** | lagoa profunda | ✅ Natural Romance postpositive order (`lagoa` vs. `lago`) |
| **old road** | antigo caminho | ✅ Never `"estrada velha"` |
| **log bridge** | ponte de toras | ✅ |
| **the whirling infinite** | o Infinito Remoinhado | ✅ Summit gateway |

### Sublocations

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| stone shelter | abrigo de pedra | |
| mountain temple | templo da montanha | |
| iron gate of the meadow | portão de ferro da campina | |
| cavernous cave of the meadow | caverna cavernosa na campina | |
| miracle of the meadow | milagre da campina | |
| titanic hollow tree | árvore oca titânica | ✅ Postpositive adjective order (natural Romance syntax) |
| parliament of trees | parlamento de árvores | ✅ Lowercase metaphor (`a parliament of trees`), not a proper noun |

---

## Items & Objects

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **The Megatome** | o Megatomo | ✅ The burdensome book (lowercase article in running prose) |
| **sword** | espada | ✅ |
| **shield** | escudo | ✅ |
| **key** | chave | ✅ Logfella's lost key |
| | | |
| **Gold Trigon** | Trígono Dourado | ✅ First trigon |
| **Bright Moon Trigon** | Trígono da Lua Radiante | ✅ Pink/bright trigon |
| **Dark Moon Trigon** | Trígono da Lua Sombria | ✅ Blue/dark trigon |
| **The Trigon Trifecta** | a Tríade Trigônica | ✅ All three trigons (lowercase article in running prose) |
| | | |
| hearth | fogo / lareira / lar | ⚠️ `lareira / lar` used in poetic/proverbial contexts |
| firewood | lenha | ✅ |
| well | poço | ✅ |
| nestbox | casa de passarinho | ✅ Matches visual birdhouse pixel art (`D079`, `D108–D109`, `D338`) |
| mushroom | cogumelo | ✅ |
| record | disco | ✅ |

---

## Gameplay Mechanics

### Core Mechanics

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **Sworcery** | espadância | ✅ Lowercase as common noun (magic/science). Cap only in Title/Intro. |
| **sworcerer** | espadancista | ✅ Practitioner of sworcery (`D280`, `D282`). Gender-invariable (`-ista`). |
| **Song of Sworcery** | Canção da Espadância | ✅ Main ability (Proper noun) |
| **sworcery aura** | aura de espadância | ✅ Visual indicator |
| **sylvan sprite** | espírito silvano | ✅ Collectible creatures |
| **sonorous spume** | sussurrantes espumas | ✅ Sprite indicators |
| **skyward beam** | feixe celestial | ✅ Trigon activation (`"feixe"`, not `"raio"`) |
| **miracle** | milagre | ✅ Special events |
| **to enact / work a miracle** | operar um milagre | ✅ Always `"operar"` (or `"farão um milagre"` in rhyme); NEVER `"obrar"` due to scatological ambiguity |

### Combat & Actions

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| press & hold / touch & hold | mantenha pressionado / segure | ✅ Primary interaction |
| tap / tip tap | pressione / tip tap (`TOCAR` on `CNTRL_TOUCH`) | ✅ Quick button press (`TOCAR` for Switch touchscreen diagram `CNTRL_TOUCH`; `toque` in narrative prose) |
| swipe | deslize | ✅ Gesture |
| move it move it | remexer (`D035`) / dar no pé (`D041`, `D321`) | ✅ Musical *Madagascar* nod in `D035`; natural haste/flight idiom in `D041` and `D321` |
| shield button | botão do escudo | ✅ With article |
| hold shield to heal (`HOLD_SHIELD_TO_HEAL`) | SEGURE PARA SE CURAR | ✅ Deliberate omission of `"shield"` to prevent horizontal collision with the sword sprite (*see [§12](#portuguese-technical-implementations--lqa-reference)*) |
| swing sword | rebata com a espada / golpeie com a espada | ✅ |
| dodge/evade | esquivar | ✅ |

### Game States

| English | Portuguese (`pt-BR`) |
|---------|----------------------|
| dream-walking (Narrator) | caminhadas oníricas |
| dream-walking (Character) | caminhar em sonhos |
| threshold of liminality | limiar da liminaridade |
| twilight realm | reino crepuscular |
| time of miracles | tempo de milagres |

---

## Story & Lore Concepts

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **woeful errand** | funesta missão | ✅ The Scythian's quest |
| **martyrdom** | martírio | ✅ The Scythian's fate |
| **deathless specter** | espectro imortal | ✅ The Gogolithic Mass |
| **heebie jeebies** | frio na espinha | ✅ Physical sensation of fear |
| **cosmic friends forever** | amigos cósmicos para sempre | ✅ Ending phrase |
| **for glory & for spite** | pela glória e por pura teimosia | ✅ Deliberate adaptation: in English gaming idiom, doing something `"out of spite / for spite"` means stubborn defiance (`"por pura teimosia"`), avoiding unintended vindictive/romantic connotations |
| **time of woe** | tempo de angústia | ✅ Session II Theme (mirrors *tempo de milagres*) |
| | | |
| linguistic thought transmission | transmissão de pensamento linguístico | ✅ |
| esoteric markings | símbolos esotéricos | ✅ Unified across `D142`, `D210`, and `D238` (Megatome contents) |
| oblique insight | visão oblíqua | ✅ The Archetype's clues |
| mythopoetic psychocosmology | psicocosmologia mitopoética | ✅ |
| set and setting | Preparação e Ambiente | ✅ Adapted concepts |

### Atmospheric Terms

| English | Portuguese (`pt-BR`) |
|---------|----------------------|
| loathsome rainbow | odioso arco-íris |
| sinister storm / sworcery | sinistra tempestade / espadância |
| grim pole / flagpole / mysteries | lúgubre poste / mastro / lúgubres mistérios |
| ominous statue / beat | estátua ominosa / ritmo ominoso |
| eerie song | arrepiante canção |
| gathering storm | iminente tempestade |
| haunted darkness | trevas assombradas |

---

## Moon Phases & Cycles

### Critical: Always use definite articles in Portuguese!

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| **The Bright Moon looms** | **A** Lua Radiante **paira** | ✅ ALWAYS with article |
| **The Dark Moon reigns** | **A** Lua Sombria **reina** | ✅ ALWAYS with article |
| crescent moon | lua crescente | ✅ |
| mood/humor of the moon | o humor da lua | ✅ |
| lunar cycle | ciclo lunar | ✅ |

### Usage Patterns

- ✅ `"Enquanto **a** Lua Radiante paira"`
- ✅ `"Enquanto **a** Lua Sombria reina"`
- ❌ Never: `"Enquanto Lua Sombria reina"` (missing article — grammatically incorrect)

### Verb Conjugations

| Phase | Portuguese Verb |
|-------|-----------------|
| Bright Moon | `paira` (present) / `pairava`, `pairasse`, `pairará` (past/future) |
| Dark Moon | `reina` (present) / `reinava`, `reinaria` (past narrative) |

---

## UI & System Terms

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| Session I, II, III | Sessão I, II, III | ✅ |
| Side A / Side B | Lado A / Lado B | ✅ |
| press play | pressione 'Jogar' | ✅ |
| equip | equipe | ✅ |
| scroll down | role | ✅ Concise imperative for Megatome tutorial |
| unsheathe / rotate | DESEMBAINHAR? / GIRAR? | ✅ |
| BELIEVE | ACREDITE | ✅ UI Action prompt |
| QUIT? (`QUIT` / `EXIT`) | SAIR? / SAIR | ✅ Constrained to 5 chars on `QUIT` slide-out tab (*see [§12](#portuguese-technical-implementations--lqa-reference)*) |

### Menu/System

| English | Portuguese (`pt-BR`) |
|---------|----------------------|
| Settings | AJUSTES |
| date & time | data e hora |
| Go Home? | INÍCIO? |
| Authorized Personnel Only | Apenas Pessoal Autorizado |

---

## Expressions & Idioms

### Hashtags

| English | Portuguese (`pt-BR`) |
|---------|----------------------|
| #helloworld | #olamundo |
| #obviously | #obvio |
| #gotmegatome | #tenhomegatomo |
| #miracles | #milagres |
| #woodchopping | #lenhando |
| #yes #no #maybe | #sim #nao #talvez |
| #woe | #angustia |
| #wetboots | #botasmolhadas |
| #loathsomerainbows | #odiososarcoiris |
| #slaughter | #matanca |

### Colloquialisms

| English | Portuguese (`pt-BR`) | Notes |
|---------|----------------------|-------|
| amirite? | Fala sério, né? / não acha? | ✅ Context: Exasperation vs Rhetorical agreement |
| Whoa | Nossa / Eita | ✅ Context dependent |
| Yikes! | Credo! / Caramba! | ✅ Ghost vs Archetype |
| Hmm... | Hmm... | ✅ Keep as is |
| cool | legal / incrível | ⚠️ Context dependent |

### Character-Specific Speech

**Dogfella / Cachorreiro:**
- English: `"Bark Bark Bark"`
- Portuguese: `"Au Au Au"`
- ✅ Maintain barking sound appropriate to Portuguese

---

## Grammar & Style Guidelines (`pt-BR`)

> For cross-language rules shared across all localizations, see [Universal Style Guidelines](../readme.md#translation-philosophy--universal-style-guidelines).

### 1. **Article Usage with Moons**
- ✅ ALWAYS use **"a"** before Lua Radiante/Sombria.
- ✅ `"Enquanto **a** Lua Radiante paira"`
- ✅ `"Enquanto **a** Lua Sombria reina"`
- ❌ **NEVER:** `"Enquanto Lua Sombria reina"` (grammatically incorrect).

### 2. **Verb Choice for Moons (`paira` vs `reina`)**
- ✅ Use **"paira"** for *Lua Radiante* and **"reina"** for *Lua Sombria* in present-tense milestone prompts (`Enquanto a Lua Radiante paira` / `Enquanto a Lua Sombria reina`), inflecting naturally (`pairava`, `pairasse`, `reinava`, `reinaria`) in narrative past and subordinate contexts.

### 3. **`Lagoa` vs `Lago`**
- **"lagoa profunda"** = deepwater pond (small body of water)
- **"lago"** = lake (large body of water)
- These are NOT interchangeable.

### 4. **"Hearth" Translation Context**
- **"fogo"** = fire (standard narrative and dialogue references)
- **"lareira / lar"** = hearth (formal/poetic contexts)
- Special phrase: **"Onde a lareira arde, o lar faz alarde"** ✅ (Poetic wordplay using rhyme and meter).

### 5. **Conjunctions vs. English Ampersands (`e` / `+` instead of `&`)**
- ✅ **Natural Conjunctions:** Replace the English stylistic `&` with the standard Portuguese conjunction **`e`** across all UI prompts (`SEGURE E DESLIZE`, `APONTAR E CLICAR`), ancient signs (`Cítia, Ciméria, Assíria e Pérsia`), and narrative prose.
- ✅ **Button Combinations:** Use **`+`** for simultaneous controller button prompts (`PRESSIONE L + R`).
- ✅ **Brand Exception:** Retain `&` exclusively in the game's proper title and official abbreviations (`Superbrothers: Sword & Sworcery EP`, `S:S&SEP`, `S&S`).
- 💡 **Trigon Collections:** Trigon collection achievements use a deadpan, two-sentence structure (`Domamos o Trígono Dourado. Somos os maiores.`) to match the dry humor of the English source.

### 6. **Formatting & Capitalization**
- Trigon names: **"Trígono Dourado"** (both words capitalized)
- Location & item names: **"o Precipício Perigoso"**, **"a Gruta Lunar"**, **"o Megatomo"**, **"a Massa Gogolítica"**, **"a Tríade Trigônica"** (proper nouns capitalized; preceding definite article in lowercase in running prose)
- Moon phases: **"Lua Radiante"** / **"Lua Sombria"** (both capitalized, preceded by lowercase article `a`)

### 7. **Majestic Plural & Gender Agreement (`Plural Majestático`)**
- **Context:** The Scythian uses the majestic plural `"we"` (`"nós"`) throughout her narration.
- **Rule:** When an adjective modifies this `"nós"`, use the masculine/unmarked plural form (e.g., `espertos`, `maiores`) even though The Scythian is female, because `"nós"` represents both The Scythian and the player.
- ✅ **Correct:** `...como tínhamos nos tornado tão espertos...` / `somos os mais espertos!`

### 8. **Postpositive Adjective Order (`árvore oca titânica`)**
- ✅ ALWAYS place descriptive adjectives after the noun in natural Romance syntax: **"árvore oca titânica"** / **"árvore titânica"**.
- ❌ NEVER use the English anteposition calque: `"titânica árvore oca"` / `"titânica árvore"`.

### 9. **Eliminating Scatological Calques (`operar milagres`)**
- ✅ ALWAYS use **"operar milagres"** (or `"farão um milagre"` in the rhyming couplet).
- ❌ NEVER use `"obrar milagres"`: in modern spoken Portuguese (`pt-BR` and `pt-PT`), *obrar* strongly connotes defecation (*evacuar/fazer cocô*), turning holy miracles into unintended comedy.

### 10. **Demonym Disambiguation (`A Citiana` vs. `citas`)**
- ✅ Protagonist: **"A Citiana"** (preserves distinct heroine identity and avoids homophonic collision with *cita* / *citar*).
- ✅ People / Tribe: **"citas / os citas"** (normalized demonym for the Scythian people).

### 11. **Narrative Imperfect vs. Punctual Sensation Verbs**
- ✅ Use the imperfect (*pretérito imperfeito*: `tínhamos a sensação`) when establishing continuous scene backdrops and ongoing impressions (e.g., `D094`: `we had a feeling` → `tínhamos a sensação`).
- ✅ When the English source marks a sudden, punctual onset (`D347` / `D352`: `We got that/the peculiar feeling`), use expressive punctual phrasing (`Sentimos a/essa estranha sensação`).

### 12. **Gender-Neutral Player Treatment in Portuguese**
While **A Citiana** is consistently feminine in narrative prose, **The Player** addressed by The Archetype avoids gender-marked adjectives or participles via five techniques (*see [Global Guide](../readme.md#translation-philosophy--universal-style-guidelines)*):
1. **Nominalization over participles:** `Confusão?` instead of `Confuso/a?`.
2. **Invariable adjectives:** `Você é especial` (invariable in gender).
3. **Verbal circumlocutions:** `se você se perder ou sentir confusão` instead of `se você estiver perdido/a`.
4. **Epicene nouns:** `pessoas compassivas e razoáveis` to avoid masculine/feminine splits.
5. **Impersonal UI & prompts:** `Tudo pronto?` instead of `Pronto/a?`; `Tem certeza de que deseja ativar...?`.

### 13. **Cursor vs. Ponteiro & Hashtag Rules**
- **Cursor vs. Ponteiro:** Use **`CURSOR`** for the on-screen visual reticle (`MOVER CURSOR`, `CENTRALIZAR CURSOR`), and **`PONTEIRO` / `APONTAR`** for the physical Joy-Con pointing device or aiming action (`SENSIBILIDADE DO PONTEIRO`, `APONTAR E CLICAR`).
- **Hashtags:** Translate and culturally adapt hashtags (`#olamundo`, `#obvio`, `#threegutrecordsprasempre`, `#odiososarcoiris`, `#trigonodomado`). Omit accents, tildes, and cedillas inside hashtags (`#olamundo`, `#nao`, `#matanca`, `#trigonodomado`, `#erratadeedicao`) to reflect authentic 2011 Twitter behavior.
- **Retro Media Terms:** Adapt quirky media phrasing naturally (`Side B` → `Lado B`, `press play` → `pressione 'Jogar'`).

### 14. **UI Dialogue Line-Length Management & Fixed-Width HUD Constraints**
- Honor fixed HUD/slide-out character budgets (`HOLD_SHIELD_TO_HEAL`, `QUIT`, `SETTINGS`, `GO_HOME`). *See [§12](#portuguese-technical-implementations--lqa-reference) and [Global Technical Constraints](../readme.md#technical-ui--engine-constraints-lqa-reference--post-mortem).*
- As a visual heuristic for the 3-line retro tweet boxes, aim to stay near or under **~140 characters total** (~42–46 characters per row) and avoid long words near line boundaries to prevent single-word orphan overflow into a 4th line (e.g., Line 97: `...e a chave parecia perdida nos sonhos.` instead of wrapping `sonhos.` into a 4th row). Because wrapping is governed by pixel width in proportional bitmap fonts, always verify visually in-game.

### Verb Strategy for `"We spied..."`

To avoid repetition of the verb `"avistar"`, use a flexible set of synonyms based on the context of the observation:

| Observation Type | Portuguese (`pt-BR`) Verbs | Usage Context |
|:---|:---|:---|
| **General Sighting (Default)** | `avistamos`, `vimos` | The base verb for a neutral observation or the first in a series. |
| **Discovery / Surprise** | `descobrimos`, `encontramos` | For finding something new, hidden, or important (e.g., a secret statue). |
| **Chance Encounter** | `nos deparamos com` | For stumbling upon an object or character unexpectedly. |
| **Focused Observation** | `observamos`, `notamos`, `reparamos em` | For looking at something more closely or noticing a subtle detail. |
| **Distant / Difficult Sighting** | `distinguimos` | For seeing something far away, in the dark, or in a crowd. |

**Rule of Thumb:** In a sequence of observations in the same area (e.g., `INFO_CABIN*`), vary the verbs to reflect the process of discovery. Start with a general `avistamos` and move to more specific verbs like `notamos` or `descobrimos`. Apply the same variation logic to common verbs like `"conseguir"` (`got`), `"dizer"` (`said`), and `"pensar"` (`thought`).

---

## Character Voice & Tone (Portuguese Nuances)

> For the base English archetype definitions, see [Global Character Voice & Tone](../readme.md#character-voice--tone).

| Character | Portuguese Name | Portuguese Nuances |
|-----------|-----------------|--------------------|
| **The Scythian** | A Citiana | **Narradora Épica e Cansada.** Usa o plural majestático (`"nós"`). Soa como a protagonista de uma saga antiga, mas com um monólogo interior moderno e sarcástico (`"aff. Outra missão de busca? Fala sério, né?"`). |
| **The Archetype** | O Arquétipo | **O Guia Erudito.** Sua linguagem é formal, quase acadêmica. Usa palavras complexas e conceitos abstratos (`"psicocosmologia mitopoética"`). Quebra a quarta parede, tratando o jogador como um participante de um experimento. |
| **Logfella** | Troncadeiro | **O Lenhador Prático.** Fala de forma simples e direta. É amigável, mas um pouco rude. Não é `"muito de histórias"` e prefere o pragmatismo (cortar lenha). Seu apelido `"Troncadeiro"` reflete sua natureza rústica. |
| **Girl (Samae)** | Samae | **A Observadora Gentil.** Seu tom é inocente, curioso e melancólico. Está conectada com o místico (espíritos, sonhos). Fala com uma simplicidade poética, em contraste com a complexidade do Arquétipo. |
| **Dogfella** | Cachorreiro | **O Cão Críptico.** Late (`"Au"`), mas seus pensamentos são surpreendentemente filosóficos ou humorísticos. O nome `"Cachorreiro"` o conecta ao estilo de `"Troncadeiro"`. |
| **The Grizzled Boor** | O Patife Grisalho | **O Antagonista Silencioso.** Não tem diálogos. Sua ameaça é percebida pelas descrições da Citiana. Seu nome `"O Patife Grisalho"` deve soar intimidador. |
| **Ghosts** | Fantasmas / Espíritos | **Os Espíritos Expositivos.** Cada fantasma conta sua tragédia. Seu tom é de lamento, arrependimento ou, às vezes, falam `"baboseiras inúteis"` irritantes. São veículos para a história do mundo. |

---

## Dialect & Regional Standards (`pt-BR`)

The Portuguese localization is written in **Brazilian Portuguese (`pt-BR`)**, while actively avoiding anatomical slang, scatological false friends, or Spanish calques so that players in any Lusophone country (Brazil, Portugal, Angola, Mozambique, Cabo Verde) can enjoy the game without unintended double meanings:

- **Pronouns, Syntax & Character Register:**
  - Uses **`você`** (not `tu`) and natural Brazilian progressive gerunds (`estou pensando`, `caminhando em sonhos`, `por ter voltado a cortar lenha`).
  - Uses natural Brazilian **proclisis** in character speech (`eu me sento`, `a tempestade se dissipou`, `onde uma mamãe pata se agitava`), while strictly avoiding sentence- or clause-initial oblique clitics (`Ele nos lembrou`, `Nós nos perguntamos`, `Pergunto-me`, `deparamo-nos`) so the syntax never reads awkwardly to other Lusophone readers.
  - Preserves formal pronoun concordance and elevated diction in **The Archetype** (`lhe`, gender-neutral `você`, `Para ser sincero`, `Pergunto-me`, `Muito bem feito!`, `que tal?`, `não é mesmo?`), while reserving colloquial Brazilian speech (`pra`, `tá`, `tipo`) for rustic/youthful/informal voices (Logfella, Samae, and casual spirits).
  - Uses analytic past forms (`havia ouvido`, `tinha visto`) in narrative prose instead of stiff synthetic pluperfects (`ouvira`, `vira`), and normative `lembrar-se de` (`Nós nos lembramos do...`, `nos lembramos de...`).
- **Console & UI Terminology (First-Party `pt-BR` Standards):**
  - Uses **`ALAVANCA` / `ALAVANCAS`** for Nintendo Switch thumbsticks (`SENSIBILIDADE: CURSOR COM ALAVANCA`, `INVERTER ALAVANCAS`, `SENSIBILIDADE DA ALAVANCA`), **`PRESSIONE` / `MANTENHA PRESSIONADO`** for physical buttons, **`TOCAR`** for touchscreen tap gestures (`CNTRL_TOUCH`), **`REDEFINIR`** for settings reset (`RESET`), **`MATAR?`** for `SLAY?`, and **`CONTROLE`** for gamepad.
- **Lexicon & Orthography:**
  - Follows PT-BR orthography (AO-1990) and circumflex/acute accentuation (`Trígono`, `psicocosmologia mitopoética`, `fenômenos`, `superépica`, `cocriar`, `20º`, `100%`) and standard Brazilian gaming/everyday vocabulary (`videogame`, `show de rock`, `controle`, `tela`, `cachoeira`, `cogumelo`, `legal`, `galera`).
- **Cross-Variant Semantic Safety (No *Portunholismos* or Unintended Innuendo):**
  - **No scatological or anatomical double meanings:** Uses **`operar milagres`** (never `obrar milagres`, which connotes defecation in Portuguese); **`estrela do rock em tempo integral`** (never `pau pra toda obra`, avoiding vulgar connotations of *pau* across the Lusophony); and **`Que desânimo!`** / **`é um fardo`** (instead of scrotal slang `Que saco!` / `é um saco`).
  - **No Spanish calques (*portunholismos*):** Uses idiomatic Portuguese expressions such as `estados de espírito` (not `estados de ânimo`), `sem parar` (not `uma e outra vez`), `Contra todas as probabilidades` (not `Contra ventos e marés`), `nos deixou meio irritados` (not `atravessados`), and `em breve ela desapareceria` (not `se iria`).

---

## Portuguese Technical Implementations & LQA Reference

> For the underlying engine behavior, sprite-collision diagnostics, Switch/PC/iOS test evidence, and Capybara Games developer notes, see [Global Technical, UI & Engine Constraints](../readme.md#technical-ui--engine-constraints-lqa-reference--post-mortem).

### 1. Fixed-Width HUD & Menu Implementations (`strings.tsv`)

| Row & Key | English Source | Portuguese (`pt-BR`) | Length & Technical Rationale |
|-----------|----------------|----------------------|------------------------------|
| `S127` (`HOLD_SHIELD_TO_HEAL`) | `HOLD SHIELD TO HEAL` | `SEGURE PARA SE CURAR` | **20 chars.** Omits `"O ESCUDO"` (which would be 29 chars and crash into the vertical sword sprite); the pulsing shield icon directly below makes the referent self-evident. |
| `S099` (`QUIT`) | `QUIT?` | `SAIR?` | **5 chars (hard cap: 5).** Fits naturally inside the slide-out exit tab without hitting the circular icon (`⊗`). |
| `S133` (`SETTINGS`) | `SETTINGS` | `AJUSTES` | **7 chars.** Avoids `CONFIGURAÇÕES` (13 chars), which crashes straight through the sliders icon (`[≡]`). |
| `S029` (`GO_HOME`) | `GO HOME?` | `INÍCIO?` | **7 chars (cap: 8).** Unreferenced prototype string. |
| `S113` (`EXIT`) | `EXIT` | `SAIR` | **4 chars (cap: 4).** Desktop PC display/graphics options only; separate UI hierarchy from `QUIT` (`S099`). |
| `S130` (`MOTION_CURSOR_SENSITIVITY`) | `MOTION CURSOR SENSITIVITY` | `SENSIBILIDADE: CURSOR POR MOVIMENTO` | **35 chars.** Retains `CURSOR` to prevent confusion with Joy-Con motion/walking speed while fitting Switch slider width. |
| `S131` (`STICK_CURSOR_SENSITIVITY`) | `STICK CURSOR SENSITIVITY` | `SENSIBILIDADE: CURSOR COM ALAVANCA` | **34 chars.** Uses Nintendo Brasil first-party term `ALAVANCA`. |
| `S177` (`POINTCLICK_CURSORSENS_NINSWITCH`) | `POINT & CLICK CURSOR SENSITIVITY` | `SENSIBILIDADE: APONTAR E CLICAR` | **31 chars.** Structured colon prefix prevents overflow into the Switch sensitivity slider widget. |

### 2. Bitmap Font Glyph Registration (`strings.tsv`)
- **`DIGIT_STRING` (`S126`):** `0123456789` (retains leading `0` stripped in `strings.en.tsv`).
- **`SPANISH_SPECIAL` (`S167`):** `Á á Â â Ã ã À à Ç ç É é Ê ê Í í Ó ó Ô ô Õ õ Ú ú Ñ ñ Ü ü ¿ ¡ º ª « » ‹ › €` (expands the Switch source to register every Portuguese uppercase/lowercase diacritic and cedilla glyph: `â ã à ç ê ô õ`; do not revert).

### 3. Multi-Platform `strings.tsv` Superset (Rows 230–236)
`portuguese/strings.tsv` retains **236 lines** (vs. 229 in Switch `strings.en.tsv`) to preserve binary schema & key-index compatibility across Switch, PC/Steam, and legacy iOS builds (*see [Global Guide](../readme.md#5-multi-platform-stringstsv-superset-236-lines-vs-229-lines-in-switch-stringsentsv--binary-schema--key-index-compatibility)*):

| Row | Key / ID | Official Capybara Games English Source | Portuguese (`pt-BR`) | Context & Platform |
|:---:|---|---|---|---|
| **230** | `TWITTER_SELECT_BUTTON` | `SELECT` | `SELECIONAR` | iOS Twitter account selection modal button |
| **231** | `TWITTER_SELECT_MSG` | `PLEASE SELECT A TWITTER ACCOUNT` | `"POR FAVOR, SELECIONE UMA CONTA DO TWITTER"` | iOS Twitter dialog prompt |
| **232** | `TWITTER_NO_ACCOUNTS` | `There are no Twitter accounts configured on this device.` | `Não há contas do Twitter configuradas neste dispositivo.` | iOS system account check message |
| **233** | `TWITTER_REQUESTING` | `REQUESTING ACCESS...` | `SOLICITANDO ACESSO...` | iOS OAuth/permission modal status |
| **234** | `TAP_QUESTION` | `TAP?` | `PRESSIONAR?` | iOS/Mobile touch tutorial prompt |
| **235** | `EXIT_TITLE` | `Exit #sworcery?` | `Sair de #espadancia?` | PC / Steam exit confirmation dialog title |
| **236** | `EXIT_PROMPT` | `Are you sure you want to exit?` | `Você realmente deseja sair?` | PC / Steam exit confirmation dialog body |

### 4. Cross-Platform & Parity Lines (`dialog.tsv`)
- **`ARCHETYPE_TREEHINT` (`D230`, 137 chars):**
  `Ao entoar a Canção da Espadância, deslize muito suavemente a aura para olhar ao redor (ou leve o cursor à borda da tela ou use as setas).`
  *(Makes aura-dragging the primary universal instruction for iOS/iPadOS & PC, followed by desktop cursor-edge/arrow controls.)*
- **`ARCHETYPE_GROTTOPARADOX` (`D494`, dead-code parity):**
  `Uma vez que o humor da lua foi alterado na Gruta Lunar, o`
  *(Retained truncated at Line 494 solely for exact `dialog.tsv` row parity.)*

### 5. Quotes, Period Placement & Acronym Formatting
- **Straight ASCII Single Quotes (`'...'`):** Always use `'...'` for internal citations, nicknames (`André, 'O Gigante'`), and UI prompts (`pressione 'Jogar'`) due to bitmap font glyph limits and TSV escaping. Keep legacy outer CSV quotes on `S090`, `S219`, `S231`.
- **Quotation-Mark Period Placement:** Inline citations embedded inside surrounding narration (`D011`, `D020`, `D132`) place the closing period **outside** the quotes (`"...".` / `'...'.`), whereas standalone full-utterance quoted transmissions and carved signs (`D004–D005`, `D068–D071`, `D081–D086`, `D145–D189`, `D531`) **intentionally keep the closing period inside the quotation marks** (`"..."`) to mirror the English TSV framing (`"""..."""`) as a consistent retro dialogue-box convention.
- **Unified Acronym:** Always use compact **`S:S&SEP`** (never `S:S&S EP`).

---

## Editorial Deviations & Transcreation Rationale (`pt-BR`)

Unlike [§12](#portuguese-technical-implementations--lqa-reference), the entries below are **purely linguistic, narrative, and stylistic editorial decisions**—not technical limitations of the game engine:

### 1. `SCYTHIAN_FOUNDATION` (`dialog.tsv` Line 508) — Narrative Slip Correction (`singular / plural`)
- **Source (`en`):** `Wait... why am I referring to myself in first person? I thought our story was told in second person? #editingoversight`
- **Portuguese (`pt-BR`):** `Espera... por que estou falando no singular? Não era para a história ser no plural? #erratadeedicao`
- **Rationale:** The English writer accidentally confused *"first-person plural"* (`we / our`) with *"second person"* (`you`). Translating literally (`primeira pessoa / segunda pessoa`) breaks the meta-joke because `"nossa história"` is first-person plural. Contrasting **`no singular` / `no plural`**—as the official 8-4 Japanese localization did—restores the intended fourth-wall joke.

### 2. Direct-Speech Explicitación & Quote Punctuation (`D145–D146`, `D150–D151`, `D156–D167`, `D170–D175`, `D178`, `D181–D182`, `D184–D185`, `D187`, `D189`, `D531`)
- **Pattern:** Portuguese adds literal double quotation marks (`"""..."""`) to direct-speech dialogue blocks spoken by ghosts/spirits (e.g., `D145`, `D150`, `D156`, `D170`, `D181`) and Samae's dream (`D531`), where the English script displays no rendered quotation marks (`D176–D177` remain unquoted because they are third-person indirect narration by The Scythian).
- **Rationale:** As documented in [Source-Script Lore Notes](../readme.md#known-source-script-quirks--lore-notes), ghosts project silent telepathic *"linguistic thought-transmissions"* in lore. Adding literal double quotes in Portuguese is **not correcting a Capybara Games typo**—it is an **intentional stylistic explicitación** for Portuguese readers, providing immediate visual clarity when a ghost's first-person singular voice (`eu`) alternates against The Scythian's surrounding first-person plural narration (`nós`). Standalone quoted boxes intentionally keep the closing period inside the quotes (`"..."`), while inline quotations (`D011`, `D020`, `D132`) place the closing period outside (`"...".` / `'...'.`).

### 3. `ARCHETYPE_GOLDMASTERINTRO` (`dialog.tsv` Line 283) — Creative Cultural License & Register Shift
- **Source (`en`):** `Confused? Excellent. Keep calm & carry on.`
- **Portuguese (`pt-BR`):** `Confusão? Palma, palma, não priemos cânico!`
- **Rationale:** Although The Archetype is normally formal and academic, this line is an **explicitly acknowledged creative license and register break**: just as the English script pivots from arcane psychocosmology into a ubiquitous British cultural meme (*"Keep calm & carry on"*), the Portuguese localization substitutes Roberto Gómez Bolaños's (*Chapolin Colorado*) beloved Brazilian dub catchphrase for immediate fourth-wall comedic impact.

---

## Cultural Adaptations (`pt-BR`)

> For full cultural context, historical background, and cross-language guidance for every allusion below, see the **[Global Cultural References Guide](../readme.md#cultural-references-pop-culture-homages--literary-allusions)**.

### 1. Cinema & Television

| Row & ID | English Source | Reference | Portuguese (`pt-BR`) Adaptation |
|---|---|---|---|
| `D103` (`INFO_WELLWHITESTAG`) | `LONG LIVE THE NEW FLESH` | *Videodrome* (1983) | `VIDA LONGA À NOVA CARNE` |
| `D108` (`INFO_NESTBOX`) | `...now home to a wretched hive.` | *Star Wars: A New Hope* (1977) | `... agora lar de uma colmeia de escória e vilania.` |
| `D132` (`INFO_ROCKSHOWGIRL`) | `...she said fire walk with me.` | *Twin Peaks* (1990–1992) | `... 'Fogo, caminha comigo'.` |
| `D375–D376` (`GCLUE_LAKESHORELAKE`) | `...I don't speak log-language.` / `...owls are not what they seem...` | *Twin Peaks* (Log Lady & The Giant) | `... não falo tronquês.` / `... às vezes as corujas não são o que parecem...` |
| `D558–D560` (`LOGFELLA_CRESCENTWANE`) | `...immortals from space who sparked in mankind...` | *2001: A Space Odyssey* (1968) | Translated with solemn, mythic-scientific phrasing (`seres imortais do espaço que despertaram na humanidade...`). |

### 2. Music, Street Art & Comics

| Row & ID | English Source | Reference | Portuguese (`pt-BR`) Adaptation |
|---|---|---|---|
| `D004` (`SIGN_TADPOL`) | `"""Home is where the hearth is."" #threegutrecords4ever"` | Three Gut Records + *heart/hearth* pun | `"""Onde a lareira arde, o lar faz alarde."" #threegutrecordsprasempre"` |
| `D035` | `...to move it move it move it.` | *"I Like to Move It"* / *Madagascar* (2005) | `nos remexer, remexer, remexer!` *(Note: `D041` & `D321` use natural haste idiom `dar no pé`.)* |
| `D127` (`INFO_CABINRECORD`) | `#theballadofthespacebabies` | Jim Guthrie OST flagship track | Kept as `#theballadofthespacebabies` |
| `D170` (`GRAVE_MEADOWGHOST*`) | `...Andre The Giant assembled a posse...` | André the Giant / Shepard Fairey | `André, 'O Gigante', juntou a galera...` |
| `D250`, `D418` (`ARCHETYPE_MEADOWHINT`, `MIRACLE1_MOUNTAINMEADOW`) | `...fold-in abilities of the great wizard Al Jaffee.` | Al Jaffee & *MAD* Fold-Ins | `os milagrosos poderes de dobra do grande mago Al Jaffee` |
| `D355` (`GCLUE_MOUNTAINMEADOW`) | `...what a dog's gotta do do.` | Turntable skip + *do-do* pun | `... o que um cão tem que fa-fa-fazer.` |
| `D404`, `D405` (`JIM_LOGFELLATHOUGHTS`) | `#1000songs` / `#andwegotolder` | Jim Guthrie discography | Kept as `#1000songs` and `#andwegotolder` |
| `D412` (`LOGFELLA_MOONGROTTOCOMMENT`) | `It's a long way from 0 to 1 & if an alien said hello it'd be in cryptic code on the stereo. Wait... what?` | Jim Guthrie – *"Hands in My Pocket"* | `Do 0 ao 1 há um longo caminho, e se um alien nos dissesse 'olá', seria em código críptico no estéreo. Pera... o quê?` |

### 3. Videogames & Tech Culture

| Row & ID | English Source | Reference | Portuguese (`pt-BR`) Adaptation |
|---|---|---|---|
| `D002` (`GIRL_TONGUES`) | `#helloworld` | Programming `"Hello, World!"` | `#olamundo` |
| `D006`, `D038` (`SIGN_CHASM`, `LOGFELLA_PRECIPICE_DONE`) | `...skyward sword...` | *Zelda: Skyward Sword* (2010 reveal) | `... uma espada apontada ao céu...` |
| `D089`, `D098`, `D251` (`INFO_BIRDEYESCULPTURE`, `ARCHETYPE_MEADOWHINT`) | `...angry bird sculpture... #subtlereference` | *Angry Birds* (2009) | `... um pássaro zangado... #sutilreferencia` |
| `D308`, `D311–D319` | `...upload The Megatome...` | Cloud computing pun (*Kingdom of the Cloud*) | `subir o Megatomo` / `subimos o Megatomo` |
| `D675` (`CREDITS`) | `S:S&S EP is a link to the past.` | *Zelda: A Link to the Past* (1991) | `S:S&SEP é um 'Link' com o passado.` |
| `D683` (`CREDITS`) | `...originally going to be called 'Poopsock'...` | MMORPG `"Poopsock"` slang | `S:S&SEP ia se chamar 'Poopsock' originalmente. Isso é totalmente verdade.` |

### 4. Literature, Philosophy, Politics & Folklore

| Row & ID | English Source | Reference | Portuguese (`pt-BR`) Adaptation |
|---|---|---|---|
| `D101–D102` (`INFO_UNWELLWELL`, `INFO_WELLNESS`) | `The well seemed unwell.` / `All's well that ends well.` | Shakespeare (c. 1604) | `O poço soltou um soluço. #poco #soluco` / `Bem está o que bem acaba.` |
| `D234` (`ARCHETYPE_MUSHROOMHINT`) | `It has even been asserted that divinatory mushrooms...` | Terence McKenna (*Stoned Ape*) | `Chegou-se a afirmar que os cogumelos adivinhatórios podem ter desempenhado um papel significativo no desenvolvimento da psique humana.` |
| `D283` (`ARCHETYPE_GOLDMASTERINTRO`) | `Confused? Excellent. Keep calm & carry on.` | British poster → *Chapolin Colorado* | `Confusão? Palma, palma, não priemos cânico!` |
| `D372–D373`, `D383` (`GCLUE_*`) | `...known unknowns & the unknown unknowns.` / `unknown nouns` | Donald Rumsfeld (2002) | `Há dois tipos de incógnitas: as incógnitas conhecidas e as incógnitas desconhecidas.` / `... os substantivos incógnitos...` |
| `D599` (`CREDITS`) | `...leadership & strategery...` | *SNL* / Will Ferrell (2000) | `... liderança e estrategeria...` |
| `D674` (`CREDITS`) | `...Robert E. Howard's sword and sorcery stories...` | Robert E. Howard | `... as histórias de espada e feitiçaria de Robert E. Howard.` |
| `D678` (`CREDITS`) | `...Carl G. Jung & his fascinating ""Red Book""...` | Carl G. Jung (*Liber Novus*) | `... Carl G. Jung e seu fascinante 'Livro Vermelho'...` |

---

## Quick Reference: Top 20 Critical Terms

| # | English | Portuguese (`pt-BR`) |
|---|---------|----------------------|
| 1 | The Scythian | A Citiana |
| 2 | Sworcery | Espadância |
| 3 | The Megatome | O Megatomo |
| 4 | sylvan sprite | espírito silvano |
| 5 | The Bright Moon looms | A Lua Radiante paira |
| 6 | The Dark Moon reigns | A Lua Sombria reina |
| 7 | woeful errand | funesta missão |
| 8 | Logfella | Troncadeiro |
| 9 | Mingi Taw | Mingi Taw |
| 10 | The Gogolithic Mass | A Massa Gogolítica |
| 11 | Trigon Trifecta | Tríade Trigônica |
| 12 | sonorous spume | sussurrantes espumas |
| 13 | dream-walking | caminhadas oníricas / caminhar em sonhos |
| 14 | the whirling infinite | Infinito Remoinhado |
| 15 | press & hold / touch & hold | mantenha pressionado / segure |
| 16 | Perilous Precipice | Precipício Perigoso |
| 17 | old road | antigo caminho |
| 18 | stone hut | cabana de pedra |
| 19 | deepwater pond | lagoa profunda |
| 20 | heebie jeebies | frio na espinha |

---

## Portuguese Translation Philosophy

> For the four overarching translation pillars and general naming strategy, see [Global Translation Philosophy](../readme.md#translation-philosophy--universal-style-guidelines).

### Neologism: `espadância`
- Treated as a lowercase common noun (like *magia* or *ciência*), capitalized only in the title/intro or the proper noun **`Canção da Espadância`**.
- The `-ância` suffix creates an abstract, mystical, and unique feel matching the game's description of sworcery as a *"consciousness expansion technique"* rather than conventional magic.
- Practitioner form: **`espadancista`** (gender-invariable `-ista`, used in `D280`, `D282`).

### Character Names: `Troncadeiro` & `Cachorreiro`
- **`Logfella` → `Troncadeiro`:** A creative rustic neologism for *"the one who deals with logs"*, reflecting Logfella's down-to-earth woodsman identity.
- **`Dogfella` → `Cachorreiro`:** Follows the exact parallel suffix structure of `"Troncadeiro"`, keeping the playful link between Logfella and Dogfella unmistakable.

---

## Version History

- **v1.0–v1.2** (2024) — Initial glossary creation, post-correction standards, and Portuguese grammar guidelines.
- **v1.3–v1.7** (2026) — Cross-lingual harmonization, in-game HUD collision LQA pass (`HOLD_SHIELD_TO_HEAL`, `QUIT`, `SETTINGS`, `SENSITIVITY`), `SPANISH_SPECIAL` Portuguese glyph registration (Row 167), multi-platform 236-row `strings.tsv` superset, `ARCHETYPE_TREEHINT` cross-platform bridge, cultural guide, and separation of technical constraints from editorial deviations.
- **v1.9** (2026) — Comprehensive MQM/LQA audit pass for `pt-BR`: standardized Nintendo Switch thumbstick terminology to Nintendo Brasil `alavanca/alavancas` (`S131`, `S136`, `S171`, `S181`, `S188`, `S205`, `S215`), shortened `CNTRL_TOUCH` → `TOCAR`, `SLAY` → `MATAR?`, and `PRESS_A_NINSWITCH` → `QUANDO QUISER`, restored `NESTES` (`S069`) and diagnostic `S232`, fixed all 6 major PT-BR patterns (`D138` tense harmony, `D184` restored `espíritos silvanos` with rhyme, `D191` past-tense narrative consistency, `D267` restored combat speed cue, `D517/520/524/539` possessives `suas`, and all 12 sentence-initial + 3 colon-initial + 3 post-comma oblique clitics per Pan-Lusophone rule), elevated Archetype register while preserving strict gender neutrality for the player (`D258`, `D275`, `D288`, `D299`, `D379`, `D462`, `D495–D496`, `D499–D500`), restored Rumsfeld pun `substantivos incógnitos` (`D372`), unified `lembrar-se de` regência, punctuation, ellipses, credits, trimmed widest narration/dialogue boxes while preserving all documented quotation marks untouched, and standardized `the whirling infinite` (`D157–D558` + `D444`) → `o Infinito Remoinhado`, `deepwater pond` → `lagoa profunda`, `nestbox` → `casa de passarinho`, `move it move it` (`D041`/`D321`) → `dar no pé`, and sheep/fatigue idioms (`à toa`, `meio moídos`).
- **v2.0** (2026) — Split the monolithic `data/locales/readme.md` into dedicated per-language documentation (`portuguese/readme.md` and `spanish/readme.md`) paired with the global technical and cultural reference in [`../readme.md`](../readme.md).

---

## Contributors & License

- **Original game text:** Superbrothers Inc., Capy Games, Jim Guthrie
- **Portuguese (`pt-BR`) localization:** [cesardeg](https://github.com/cesardeg)

For questions, corrections, or additions to this glossary, please submit issues to the repository.

This translation glossary is provided as reference documentation for the *Superbrothers: Sword & Sworcery EP* localization project. Usage rights follow the game's original licensing terms.
