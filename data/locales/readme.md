# Localization Guide & Technical Reference: Sword & Sworcery EP

---

## Purpose & Architecture

This document is the **global, language-agnostic reference** for all *Superbrothers: Sword & Sworcery EP* localizations in `data/locales/`. It documents universal style principles, character voice archetypes, empirical engine/UI constraints, source-script quirks, and cross-language cultural allusions applicable to **any** language (existing or community-contributed).

Language-specific glossaries, grammar rules, dialect standards, and localized LQA decisions live in each locale's dedicated documentation:

### Language-Specific Guides

| Locale | Language / Variant | Guide | Files |
|--------|--------------------|-------|-------|
| **`spanish/`** | Neutral Latin American Spanish (`es-419`) | **[`spanish/readme.md`](spanish/readme.md)** | [`dialog.tsv`](spanish/dialog.tsv), [`strings.tsv`](spanish/strings.tsv) |
| **`portuguese/`** | Brazilian Portuguese (`pt-BR`) | **[`portuguese/readme.md`](portuguese/readme.md)** | [`dialog.tsv`](portuguese/dialog.tsv), [`strings.tsv`](portuguese/strings.tsv) |

### Directory Overview

- **`english-vo/`** — Clean Nintendo Switch English source tables (`dialog.en.tsv`, `strings.en.tsv`, 229 rows).
- **`all-vo/`** — Capybara Games multi-language master spreadsheets (`dialog.tsv`, `strings.tsv`) including internal `FIGS Notes` and `Craig's Notes` / developer comments.
- **`spanish/` & `portuguese/`** — Actively maintained community localizations with full 236-row multi-platform `strings.tsv` compatibility and dedicated style guides.
- **`french/`, `italian/`, `japanese-vo/`, `russian/`** — Additional locale tables in the repository.
- **`../fonts/`** — Custom bitmap font modifications required for uppercase/lowercase accented glyphs and Cyrillic support (*see [`data/fonts/readme.md`](../fonts/readme.md)*).

### Target Audience
- Translators, localization teams, and QA testers working on any language
- LQA/MQM auditors evaluating engine compliance and technical playability
- Community translators, modders, and documentation writers

---

## Table of Contents
1. [Translation Philosophy & Universal Style Guidelines](#translation-philosophy--universal-style-guidelines)
2. [Character Voice & Tone](#character-voice--tone)
3. [Technical, UI & Engine Constraints (LQA Reference & Post-Mortem)](#technical-ui--engine-constraints-lqa-reference--post-mortem)
4. [Known Source-Script Quirks & Lore Notes](#known-source-script-quirks--lore-notes)
5. [Cultural References, Pop-Culture Homages & Literary Allusions](#cultural-references-pop-culture-homages--literary-allusions)
6. [Version History](#version-history)
7. [Contributors & Acknowledgments](#contributors--acknowledgments)
8. [License](#license)

---

## Translation Philosophy & Universal Style Guidelines

### Core Approach
All localizations of *Superbrothers: Sword & Sworcery EP* prioritize:
1. **Poetic/epic tone** appropriate to the classic sword-and-sorcery genre
2. **Cultural adaptation** over stiff literal translation
3. **Consistency** in canonical terminology across the entire game
4. **Playability** — UI prompts and gameplay instructions must remain unmistakable in context

### Universal Style Rules

#### 1. **Hashtags & Social Media Aesthetic**
- **Translate and culturally adapt hashtags:** Localize in-game hashtags creatively to preserve the game's witty, meta-textual 2011 Twitter aesthetic for native audiences. (The original European FIGS release left hashtags untranslated in English, which broke immersion.)
- **2011 Twitter parsing authenticity:** Omit acute accents or diacritics on vowels inside hashtags where appropriate in your target language to mirror 2011 Twitter hashtag behavior, while preserving language-essential letters where natural.
- **Music/track Easter egg exceptions:** Leave official soundtrack and discography hashtags (`#theballadofthespacebabies`, `#1000songs`, `#andwegotolder`) and label names (`threegutrecords`) intact so references stay recognizable.
- **Retro media terms:** Adapt quirky physical-media phrasing naturally (e.g., `Side A / Side B`, `press play`).

#### 2. **Proper Nouns & Titles**
- **Never translate:** `Jim Guthrie`, `André`, `Samae`, `Mingi Taw`, `Al Jaffee`, `Robert E. Howard`, `Carl G. Jung`.
- **Translate epithets and titles:** e.g., `"The Giant"`, `"The Archetype"`, `"The Grizzled Boor"`, `"The Kingdom of the Cloud"`.

#### 3. **Emphasis & Tone**
- Maintain a poetic, mythic, slightly archaic tone in narrative prose.
- Keep a casual, rustic, or deadpan tone in character dialogue and inner monologue.
- Preserve humor, dry irony, and wordplay wherever possible.

#### 4. **Neologism & Character-Naming Strategy**
- **`Sworcery`:** Core neologism — never replace it with generic `"magic"`. Treat it as a lowercase common noun (like `"magic"` or `"science"`), capitalized only in the title/intro or the proper ability title **`Song of Sworcery`**.
- **`Logfella` & `Dogfella`:** `Logfella` is playful wordplay combining `"fella"` + wood/logs, and `Dogfella` mirrors it as a parallel construction. Aim for a matching pair of rustic nicknames using the same morphological pattern in your target language.

#### 5. **Consistency Over Variation**
- Use the exact same canonical term throughout for key mechanics, locations, items, and lore concepts.
- Variation is acceptable only for:
  - Grammatical requirements (verb conjugations, inflections)
  - Avoiding repetition in the same paragraph or consecutive lines
  - Intentional character voice differences

#### 6. **Observation Verb Variation (`"We spied..."`)**
- Avoid repeating a single verb for `"We spied..."` across sequences of scene observations (e.g., `INFO_CABIN*`).
- Vary verbs according to context: general sighting, discovery/surprise, chance encounter, focused observation, and distant/difficult sighting.
- Apply the same variation strategy to frequently repeated verbs such as `got`, `said`, and `thought` to keep The Scythian's narration lively.

#### 7. **Gender-Neutral Player Treatment & Majestic Plural**
The game makes a strict distinction between two grammatical referents:
- **The Scythian (The Protagonist):** A female warrior, consistently referred to with feminine grammar in third-person narrative references.
  - **Majestic Plural (`we`):** Throughout her narration, The Scythian uses the majestic plural `"we"`, intentionally blending herself and the player. In languages with grammatical gender on plural adjectives, use the unmarked/inclusive plural form rather than feminine-only plural so non-female players remain immersed in the shared `"we"`.
- **The Player (The Participant):** The real person addressed directly by The Archetype breaking the fourth wall. In gendered languages, avoid gender-marked adjectives or participles when addressing the player by using five core techniques:
  1. **Nominalization over participles** (e.g., noun `"Confusion?"` instead of gendered `"Confused?"`).
  2. **Invariable adjectives** (adjectives that do not inflect for gender).
  3. **Verbal circumlocutions** (e.g., `"if you lose your way or feel confused"` instead of gendered `"lost"`).
  4. **Epicene nouns** (e.g., `"compassionate and reasonable people"` instead of gendered forms).
  5. **Impersonal UI & prompts** (e.g., `"All set?"` instead of gendered `"Ready?"`).

#### 8. **Cursor vs. Pointer (Hardware vs. Visual)**
- **Cursor:** Always refers to the visual reticle/element moving on screen (e.g., `MOVE CURSOR`, `CENTER CURSOR`).
- **Pointer:** Always refers to the physical Joy-Con acting as a pointing device, or the action of aiming it (e.g., `POINTER SENSITIVITY`, `POINT & CLICK`). Do **not** use `"cursor"` to refer to the physical hardware.

#### 9. **Conjunctions vs. English Ampersands (`&`)**
- Replace the English stylistic `&` with your target language's natural conjunction in UI prompts, carved signs, and prose.
- Use **`+`** for simultaneous controller button combinations (e.g., `L + R`).
- Retain **`&`** exclusively in the game's proper title and official abbreviations (`Superbrothers: Sword & Sworcery EP`, `S:S&SEP`, `S&S`).

---

## Character Voice & Tone

This table defines the baseline personality and speaking style for each character across all languages. See [`spanish/readme.md`](spanish/readme.md#character-voice--tone-spanish-nuances) and [`portuguese/readme.md`](portuguese/readme.md#character-voice--tone-portuguese-nuances) for language-specific voice nuances.

| Character | Voice & Tone |
|-----------|--------------|
| **The Scythian** | **The Stoic Narrator.** Uses `"we"` (*pluralis majestatis*). Her tone is epic, descriptive, and poetic, punctuated by flashes of dry, modern humor and sarcastic inner monologue. She is on a `"woeful errand"` yet often sounds cynical or unimpressed. |
| **The Archetype** | **The Erudite Guide.** Speaks formally, almost academically. Uses complex, philosophical, and fourth-wall-breaking language (`"mythopoetic psychocosmology"`). He is the director of the `"experience"`, addressing the player as a participant in an experiment. |
| **Logfella** | **The Practical Woodsman.** Simple, direct, and down-to-earth. Friendly but gruff, with a `"low tolerance for lore"` and a focus on practical matters like chopping wood and staying warm. His speech is colloquial and rustic. |
| **Girl (Samae)** | **The Gentle Observer.** Innocent, curious, and deeply connected to the mystical world (sprites, dreams, moon moods). Her tone is soft, observant, and sometimes melancholic (`"feeling the woe"`), contrasting poetic simplicity against The Archetype's complexity. |
| **Dogfella** | **The Cryptic Canine.** Mostly barks (adapt the onomatopoeia naturally to the target language), but his `"barks"` translate into surprisingly profound or humorous philosophical wisdom when The Scythian can understand him. |
| **The Grizzled Boor** | **The Silent Antagonist.** Has no dialogue. His menacing, brutish presence is communicated exclusively through his actions and The Scythian's descriptions. |
| **Ghosts** | **The Expositional Spirits.** Each ghost recounts a past tragedy. Their tone is sorrowful, regretful, or occasionally filled with irritatingly unhelpful `"nonsense"`, serving as vehicles for world lore. |

---

## Technical, UI & Engine Constraints (LQA Reference & Post-Mortem)

This section serves as an empirical **LQA post-mortem and technical changelog** applicable to all languages. It documents strictly technical engine constraints—UI layout collisions, font atlas glyph registration, binary schema compatibility, TSV escaping, and cross-platform input behavior—backed by live in-engine testing across Nintendo Switch, PC (Steam), and iOS, alongside official internal developer notes from Capybara Games (`FIGS Notes` / `Craig's Notes` in `all-vo/strings.tsv` and `all-vo/dialog.tsv`).

### 1. `HOLD_SHIELD_TO_HEAL` (`strings.tsv` Line 127) — Deliberate Omission of `"Shield"`
- **Source (`en`):** `HOLD SHIELD TO HEAL` (19 characters)
- **Technical Evidence:**
  1. **Single-line non-wrapping HUD element:** In combat, the engine renders `HOLD_SHIELD_TO_HEAL` on a single horizontal line that **does not wrap** to a second row.
  2. **Sprite collision with the sword:** The text is centered directly over the glowing shield icon (`[ ▣ ]`) and sits immediately to the left of the vertical sword sprite (`|`). Even at **19–20 characters**, the right edge sits just pixels away from the sword blade. Longer strings (~29 characters when including the word `"shield"`) crash directly through the sword sprite.
  3. **Visual redundancy:** Because the label is anchored directly above the pulsing shield icon, omitting the noun `"shield"` keeps the HUD collision-free while the visual referent remains self-evident.

### 2. `QUIT` (`Line 99`), `SETTINGS` (`Line 133`), `GO_HOME` (`Line 29`) & `EXIT` (`Line 113`) — Slide-Out Tabs vs. Menu Hierarchy
- **`QUIT` (`strings.tsv` Line 99):**
  - **Source (`en`):** `QUIT?` (5 characters) | **Hard Limit:** `Max characters: 5` (explicitly set by Capybara Games in `all-vo/strings.tsv`, Row 99).
  - **In-game sprite overlap:** Renders inside a narrow grey slide-out tab on the far-left edge terminated with an embedded circular button icon (`⊗`). Exceeding 5 characters (for instance, adding inverted punctuation to reach 7 characters) crashes directly through the circular icon.
- **`SETTINGS` (`strings.tsv` Line 133):**
  - **Source (`en`):** `SETTINGS` (8 characters)
  - **In-game sprite overlap:** On the title screen, `SETTINGS` renders inside a fixed-width grey slide-out pill on the left edge with an embedded sliders icon (`[≡]`) on its right end, sized for an ~8-character word. Long translations (~13 characters) crash straight through the sliders icon and spill onto the background—a bug that actually shipped in the official European `ES_FIGS` and `DE_FIGS` releases. Target **≤ 8 characters**.
- **`GO_HOME` (`strings.tsv` Line 29):**
  - **Source (`en`):** `GO HOME?` (8 characters) | **Limit:** `8`
  - **Developer Note:** In `all-vo/strings.tsv` (Row 29), developer Matt Repetski (`MR`) explicitly noted: *"IT: What's the context/function of this string? MR - I think it's actually not being called, but in case we need it a literal translation would likely be fine."* `GO_HOME` is an **unreferenced prototype string** that never renders in the active in-game slide-out tab.
- **Differentiating `QUIT` (Line 99) vs. `EXIT` (Line 113):**
  - `QUIT` (`Line 99`) operates inside the in-game gameplay pause tab.
  - `EXIT` (`Line 113`, `Max characters: 4`) operates exclusively in the desktop PC display/graphics options screen (alongside `RESOLUTION`, `RESET`, `APPLY`, `BACK`).
  - Because `QUIT` and `EXIT` exist in completely distinct UI hierarchies and screens, using the same base verb mirrors standard OS conventions without runtime collision or player ambiguity.

### 3. Sensitivity Controls: Motion, Analog Stick & Point-and-Click (`strings.tsv` Lines 130, 131, 177)
- **Keys & English Source:**
  - `MOTION_CURSOR_SENSITIVITY` (`Line 130`): `MOTION CURSOR SENSITIVITY`
  - `STICK_CURSOR_SENSITIVITY` (`Line 131`): `STICK CURSOR SENSITIVITY`
  - `POINTCLICK_CURSORSENS_NINSWITCH` (`Line 177`): `POINT & CLICK CURSOR SENSITIVITY`
- **Technical & Design Evidence:**
  1. **Retain `"Cursor"` to Prevent Semantic Collision:** Omitting `"cursor"` in Nintendo Switch menus generates critical confusion between Joy-Con physical gyroscopic movement, character walking speed, and reticle aiming. Retaining the word for `CURSOR` guarantees players know which input layer is being tuned.
  2. **Menu Box Width Limit (~35-character threshold on Switch):** On Nintendo Switch, the settings menu renders each option label immediately to the left of the sensitivity slider widget. Literal translations exceeding ~35 characters (e.g., ~45 chars) overflow into the slider handle. Structuring all three controls with a concise colon prefix (`[SENSITIVITY]: [MODE]`) differentiates the three control schemes cleanly while staying within ~35 characters.

### 4. `DIGIT_STRING` (Line 126) & `SPANISH_SPECIAL` (Line 167) — Bitmap Font Glyph Registration
- **`DIGIT_STRING` (`strings.tsv` Line 126):**
  - **Source (`strings.en.tsv`):** `123456789` → **Required localized value:** `0123456789`
  - **Developer Evidence:** `strings.en.tsv` shows `123456789` only because spreadsheet auto-formatting stripped the leading `0` when the English column was exported from Excel. Capybara Games' official localization sheet (`FIGS Notes`, row 126) explicitly instructs localizers: *"This string used to automatically delete 0s at the beginning of the string because of formatting, so they must be re-added manually."* Removing `0` breaks character-set registration for the digit `0`.
- **`SPANISH_SPECIAL` / `*_SPECIAL` (`strings.tsv` Line 167):**
  - **Source (`strings.en.tsv`):** `Á É Í Ó Ú Ñ Ü ¿ ¡ º ª « » ‹ › €` *(uppercase vowels/`Ñ`/`Ü` only)*
  - **Technical Evidence:** Just like `DIGIT_STRING`, the `*_SPECIAL` rows declare special glyphs for bitmap font atlas/table registration. Because the official Switch source omitted lowercase accented vowels and language-specific diacritics (such as Portuguese `â ã à ç ê ô õ`), localizations **must expand Row 167** to include every uppercase and lowercase special glyph required by the target language. Do not revert Row 167 to the truncated uppercase-only source string. See also [`data/fonts/readme.md`](../fonts/readme.md) for custom Conduit ITC uppercase glyph remapping.

### 5. Multi-Platform `strings.tsv` Superset (236 Lines vs. 229 Lines in Switch `strings.en.tsv`) — Binary Schema & Key-Index Compatibility
- **Structure:** Switch `strings.en.tsv` contains **229 lines**, whereas unified multi-platform builds require **236 lines**.
- **Technical Evidence:**
  - Lines 1–229 match Nintendo Switch `strings.en.tsv` 1-to-1 by key and row number.
  - Lines 230–236 are **7 legacy iOS and PC/Steam keys** stripped when Twitter integration and desktop exit dialogs were removed on Switch.
  - **Binary Schema Compatibility:** Retaining the full 236-key superset preserves lookup-table index compatibility across Nintendo Switch, PC (Steam), and legacy iOS/mobile binaries, allowing one unified `.tsv` per language to serve as a drop-in patch without missing-key runtime exceptions.
  - *(Empirical verification)*: Testing on vintage hardware (an iPod Touch running iOS 4 with the original 2011 Twitter-enabled build) confirmed that the mobile executable crashes immediately if any of these 7 keys are missing from `strings.tsv`.
- **Official Capybara Games English Source Reference (Rows 230–236):**

| Row | Key / ID | Official Capybara Games English Source | Context & Platform |
|:---:|---|---|---|
| **230** | `TWITTER_SELECT_BUTTON` | `SELECT` | iOS Twitter account selection modal button |
| **231** | `TWITTER_SELECT_MSG` | `PLEASE SELECT A TWITTER ACCOUNT` | iOS Twitter dialog prompt *(keep outer CSV quotes if comma present)* |
| **232** | `TWITTER_NO_ACCOUNTS` | `There are no Twitter accounts configured on this device.` | iOS system account check message |
| **233** | `TWITTER_REQUESTING` | `REQUESTING ACCESS...` | iOS OAuth/permission modal status |
| **234** | `TAP_QUESTION` | `TAP?` | iOS/Mobile touch tutorial prompt |
| **235** | `EXIT_TITLE` | `Exit #sworcery?` | PC / Steam exit confirmation dialog title |
| **236** | `EXIT_PROMPT` | `Are you sure you want to exit?` | PC / Steam exit confirmation dialog body |

### 6. `ARCHETYPE_TREEHINT` (`dialog.tsv` Line 230) — Cross-Platform Camera Mechanics (Mobile Touch vs. Desktop Edge-Hover & Keys)
- **Source Text Evolution:**
  - **Original iOS (2011):** `Once you have begun to sing a song of sworcery you can ever-so-gently touch & swipe on the sworcery aura to look around.`
  - **PC / Steam (`dialog.en.tsv` Line 230, tagged `Old PC Version`):** `Once you have begun to sing a song of sworcery you can ever-so-gently touch the edge of the screen to look around (or use the arrow keys).`
  - **Nintendo Switch (`ARCHETYPE_TREEHINT_NINSWITCH`, Line 233):** `Once you have begun a song of sworcery you may want to look around and take in your surroundings.` *(Developer note by Matt Repetski: "Switch will need its own most likely. Should cover moving camera with cursor, arrows/d-pad and also touch and drag...")*
- **Technical & Design Evidence:**
  1. **Unified Multi-Platform Deployment:** The exact same `dialog.tsv` table is compiled into both PC (Steam) and mobile (iOS & iPadOS) distributions.
  2. **Total Breakdown of PC Instructions on Mobile (iOS / iPadOS):** On iOS/iPadOS, even when an external mouse, trackpad, or physical keyboard is paired to an iPad, the mobile engine's touch-input layer **does not process edge-of-screen cursor hovering or arrow keys for camera panning**. Dragging the sworcery aura (*touch & swipe*) is the **sole functional method** on touch devices. Translating the Steam string literally completely misleads mobile players.
  3. **Desktop Ambiguity on PC/Steam:** The English PC wording (`"touch the edge of the screen"`) is technically imprecise on desktop (the camera pans by hovering the cursor near the screen border or pressing arrow keys), while clicking and gently dragging the sworcery aura **remains fully active and functional on PC**.
  4. **Recommended Cross-Platform Editorial Bridge:** Make **aura swiping/dragging the primary universal instruction** (works identically with a finger on mobile and a mouse drag on PC), followed by a concise parenthetical covering desktop cursor-edge hovering and arrow keys, keeping total length ≤ ~140 characters to fit the 3-line box.

### 7. `ARCHETYPE_GROTTOPARADOX` (`dialog.tsv` Line 494) — Unreferenced Dead Code Row Parity
- **Source (`en`):** `Once the moods of the moon have been altered in The Moon Grotto the`
- **Developer Evidence:** Truncated mid-sentence in the original English script. In `all-vo/dialog.tsv` (`FIGS Notes`, row 494), developer Matt Repetski confirmed: *"This is not actually being called, ignore it."* Retain a placeholder/parity line at Row 494 solely to preserve exact row parity across `dialog.tsv`.

### 8. Bitmap Font Glyph Limits & TSV Parser Escaping (`'...'` vs. `«...»` / `“...”`)
- **Rule:** Always use **single straight ASCII quotes (`'...'`)** for internal quotes, nicknames, UI prompts, and cited words inside dialogue.
- **Technical Evidence:**
  1. **Bitmap font glyph limitations:** Although `SPANISH_SPECIAL` (Line 167) includes `« » ‹ ›` in the string table, the game's compiled bitmap fonts (`conduit_itc_2x.fnt`, `arial_narrow.fnt`) lack typographic curly quotes (`“ ” ‘ ’`) and single angle quotes (`‹ ›`).
  2. **TSV parser behavior:** Standard CSV/TSV cell quoting wraps fields containing commas or quotes in straight double quotes (`"..."`), escaping internal literal double quotes as `""`. Using single ASCII quotes `'...'` for inline citations avoids escaping errors and renders cleanly across all bitmap fonts. Retain existing outer CSV quotes on legacy/imported `strings.tsv` rows (`S090`, `S219`, `S231`) for parser stability.

### 9. Proportional Font Wrapping Heuristic (~140 chars), `S:S&SEP` Acronym & LIFO Dialogue Stack
- **Proportional Bitmap Font Wrapping (~140 chars heuristic):** Because `conduit_itc_2x.fnt` and `arial_narrow.fnt` are **proportional bitmap fonts** (not monospaced), actual line breaks in the 3-line tweet box depend on cumulative pixel width rather than raw character count—a 136-character string rich in wide uppercase glyphs (`M`, `W`, `G`) can wrap onto a 4th line earlier than a 142-character string rich in narrow glyphs (`i`, `l`, spaces). Treat **~140 characters total** (~42–46 per row) as an empirical safe heuristic and always verify visually in-game.
- **Unified `S:S&SEP` Acronym:** While `dialog.en.tsv` inconsistently mixes `S:S&SEP` and `S:S&S EP`, standardize on the compact form **`S:S&SEP`** across all UI and dialogue boxes to save horizontal pixel width and ensure consistency.
- **LIFO (Bottom-to-Top) Dialogue Stack:** Several multi-line blocks (`ARCHETYPE_FOUNDATION` `D056–D067`, `GCLUE_*`, `ARCHETYPE_*TRIGONCOLLECTED` `D486–D488`) are pushed onto an engine stack and displayed **from bottom to top** (e.g., `D066 → D065 → D064 → D063 → D062`). Always verify pronoun antecedents and logical flow in actual in-game reading order rather than top-to-bottom TSV row order.
- **iOS Missing Credit Logos Filter:** Keep `Logos/DolbyDigital` and `Logos/DigitalSurround` rows intact in `data/locales/*/dialog.tsv` (Steam requires them); the iOS build pipeline filters them automatically during packaging (*see [`tools/ios/readme.md`](../../tools/ios/readme.md)*).

---

## Known Source-Script Quirks & Lore Notes

These are notable peculiarities in the original English script—not engine bugs—that every translator should understand before localizing:

### 1. `SCYTHIAN_FOUNDATION` (`dialog.tsv` Line 508) — Original Narrative Slip
- **Source (`en`):** `Wait... why am I referring to myself in first person? I thought our story was told in second person? #editingoversight`
- **Issue:** The original English writer accidentally confused *"first-person plural"* (`we / our`) with *"second person"* (`you`). Throughout the game, The Scythian narrates in the **first-person plural**, and in `D508–D510` she momentarily slips into the **first-person singular** (`I / my`).
- **Recommendation:** Translating `"first person / second person"` literally breaks the meta-joke for observant readers. Contrasting **singular vs. plural** (the solution used by the official 8-4 Japanese localization, as well as our Spanish and Portuguese localizations) restores the intended fourth-wall joke.

### 2. Direct-Speech Quotation Lore (`dialog.tsv`)
- In the English original, living characters (`Logfella`, `Samae`) do **not** display rendered quotation marks (`D531` in `dialog.en.tsv` has only outer CSV field quotes due to an internal comma). Literal quotes in English appear only on carved signs (`D004–D005`) and selected Archetype transmissions (`D068–D071`, `D081–D086`).
- Within the game's lore (`D067`, `D069`) and credits (`D594–D596`), only The Scythian, Logfella, and The Archetype have vocal performances; ghosts project silent telepathic *"linguistic thought-transmissions"* intercepted via The Megatome.
- Localizations may optionally add literal double quotation marks (`"""..."""`) around ghost direct speech (`D145–D189`, excluding third-person narration `D176–D177`) and Samae's dream (`D531`) as a stylistic explicitación to visually separate first-person ghost speech from The Scythian's surrounding plural narration. Doing so has zero effect on engine behavior.

---

## Cultural References, Pop-Culture Homages & Literary Allusions

*Superbrothers: Sword & Sworcery EP* blends Iron Age Scythian myth with dense layers of cinema, indie music, comic-book, videogame, and countercultural allusions. This cross-language catalog identifies every cultural wink in `dialog.tsv` so translators porting the game into any language can adapt it faithfully. For concrete localized examples, see [`spanish/readme.md`](spanish/readme.md#cultural-adaptations-es-419) and [`portuguese/readme.md`](portuguese/readme.md#cultural-adaptations-pt-br).

### 1. Cinema & Television

| Row & ID | English Source | Cultural Reference & Context | Localization Advice |
|---|---|---|---|
| `D103` (`INFO_WELLWHITESTAG`) | `LONG LIVE THE NEW FLESH` | **David Cronenberg's *Videodrome* (1983):** Max Renn's final mantra before transcending his physical body. | Use the official localized dub/subtitle quote from *Videodrome* in your target language. |
| `D108` (`INFO_NESTBOX`) | `We spied a curious-looking nestbox, now home to a wretched hive.` | ***Star Wars: Episode IV – A New Hope* (1977):** Obi-Wan Kenobi describing Mos Eisley (*"You will never find a more wretched hive of scum and villainy"*), playing on a literal wasp/bee *hive* inside the birdhouse. | Echo the canonical *Star Wars* phrasing for *"hive of scum and villainy"* so the pun on a literal insect hive is unmistakable. |
| `D132` (`INFO_ROCKSHOWGIRL`) | `At a rock show we spied Samae & we thought maybe she said fire walk with me.` | **David Lynch's *Twin Peaks* (1990–1992):** The iconic poem (*"Fire, walk with me"*) and prequel film *Twin Peaks: Fire Walk with Me*. | Preserve the exact canonical *Twin Peaks* phrasing in your language, even if its imperative pronoun form differs from the rest of the script. |
| `D375–D376` (`GCLUE_LAKESHORELAKE`) | `My logs have many secrets... Unfortunately I don't speak log-language.` / `In my experience there are times when owls are not what they seem...` | **David Lynch's *Twin Peaks* (The Log Lady & The Giant):** A double homage in the same LIFO dialogue block. First (`D376`), Logfella echoes The Giant's warning to Agent Cooper (*"The owls are not what they seem"*); second (`D375`), Logfella—who, like Margaret Lanterman (**The Log Lady**), carries a log in his arms everywhere—parodies her famous introductions (*"My log has something to tell you"* / *"My log saw something"*), joking that his logs hold secrets too, except he doesn't speak `"log-language"`. | Coin a playful language name derived from the word for *log* in `D375`, and match the canonical *Twin Peaks* owl quote in `D376`. |
| `D558–D560` (`LOGFELLA_CRESCENTWANE`) | `...from whence The Megatome had come in a distant Stone Age. He spoke of immortals from space who sparked in mankind...` | **Arthur C. Clarke & Stanley Kubrick's *2001: A Space Odyssey* (1968):** The extraterrestrial Monolith arriving in the Stone Age ("The Dawn of Man") to spark human intelligence. | Keep the solemn, mythic-scientific cosmic-horror register of Clarke's Monolith mythos. |

### 2. Music, Street Art & Comics

| Row & ID | English Source | Cultural Reference & Context | Localization Advice |
|---|---|---|---|
| `D004` (`SIGN_TADPOL`) | `"""Home is where the hearth is."" #threegutrecords4ever"` | **Three Gut Records:** The influential Canadian independent record label co-founded by composer Jim Guthrie in Guelph/Toronto (1999–2005). Also a pun on *"Home is where the heart is"* vs. *"hearth"* (fireplace). | Keep `threegutrecords` intact in the hashtag and recreate the *heart/hearth* wordplay with a warm proverb or rhyme about fire/hearth and home. |
| `D035` | `...to move it move it move it.` | **Reel 2 Real feat. The Mad Stuntman – *"I Like to Move It"* (1993):** Eurodance classic popularized globally by King Julien in DreamWorks' *Madagascar* (2005). *(Note: `D041` and `D321` are best rendered with natural haste/flight idioms rather than dance phrasing.)* | Use the recognizable localized hook from the *Madagascar* dub in your language for the triple-repetition line `D035`. |
| `D127` (`INFO_CABINRECORD`) | `...above the hearth. #theballadofthespacebabies` | ***"The Ballad of the Space Babies"*:** Flagship track on Jim Guthrie's *Sword & Sworcery LP: The Ballad of the Space Babies* soundtrack. | Leave the song title hashtag in English so it links directly to the official track title. |
| `D170` (`GRAVE_MEADOWGHOST*`) | `Last year before the yuletide Andre The Giant assembled a posse...` | **André the Giant & Shepard Fairey's *"Andre the Giant Has a Posse"* (1989):** Dual nod to legendary wrestler/actor André the Giant (*The Princess Bride*) and Shepard Fairey's street-art sticker campaign (*OBEY*). | Translate the epithet (`The Giant`) while keeping `André` recognizable. |
| `D250`, `D418` (`ARCHETYPE_MEADOWHINT`, `MIRACLE1_MOUNTAINMEADOW`) | `...the miraculous fold-in abilities of the great wizard Al Jaffee.` / `...in the fold-in fashion of the mad wizard Al Jaffee.` | **Al Jaffee (1921–2023) & *MAD Magazine* Fold-Ins:** Jaffee created the back-cover *MAD Fold-In*, where folding the page inward brings two distant edges together to form a new image—the exact gameplay mechanic of the Meadow Miracle. | Keep **Al Jaffee** untouched and use the word for *folding* a page so the visual puzzle hint remains clear. |
| `D355` (`GCLUE_MOUNTAINMEADOW`) | `...a dog's gotta do what a dog's gotta do what a dog's gotta do do.` | **Turntable record-skip / sample loop + *"do-do"* (poop) pun:** Parodies the western cliché *"A man's gotta do what a man's gotta do"* while stuttering like a vinyl record or hip-hop scratch (`do-do`). | Recreate the rhythmic vinyl-stutter at the end of the repeated verb. |
| `D404`, `D405` (`JIM_LOGFELLATHOUGHTS`) | `#1000songs` / `#andwegotolder` | **Jim Guthrie's discography:** References his *1000 Songs* project and his indie track *"And We Got Older"* (from *Now, More Than Ever*, 2003). | Keep the English song/project hashtags intact as musical Easter eggs. |
| `D412` (`LOGFELLA_MOONGROTTOCOMMENT`) | `It's a long way from 0 to 1 & if an alien said hello it'd be in cryptic code on the stereo. Wait... what?` | **Jim Guthrie – *"Hands in My Pocket"* (*Now, More Than Ever*, 2003) & Moon Grotto SSTV/audio cipher:** Paraphrases Guthrie's lyrics while hinting at the hidden audio transmission in the Moon Grotto. | Preserve the internal rhyme or cadence (`hello / stereo`, `0 to 1`) and the confused `Wait... what?` punchline. |

### 3. Videogames & Tech Culture

| Row & ID | English Source | Cultural Reference & Context | Localization Advice |
|---|---|---|---|
| `D002` (`GIRL_TONGUES`) | `...in a sunlit meadow. #helloworld` | **`"Hello, World!"`:** The canonical first string printed when learning a programming language or booting a new system (used on the very first line of the game). | Use the standard programming `"Hello, World!"` equivalent in your language. |
| `D006`, `D038` (`SIGN_CHASM`, `LOGFELLA_PRECIPICE_DONE`) | `...a stone carved with the glyph of a skyward sword...` / `...the nearby glyph depicting the skyward sword.` | ***The Legend of Zelda: Skyward Sword* (unveiled at E3 June 2010):** Nintendo revealed *Skyward Sword* (and Link's signature gesture of raising his sword skyward to charge a beam) while *S:S&SEP* was in full production in 2010; the Scythian's own sword-raising mechanic and this phrasing are a direct contemporary nod. | Since *Skyward Sword* was rarely translated in Nintendo's localized game titles, render the image naturally and poetically. |
| `D089`, `D098`, `D251` (`INFO_BIRDEYESCULPTURE`, `ARCHETYPE_MEADOWHINT`) | `We spied an angry bird sculpture looming above the meadow. #subtlereference` | **Rovio's *Angry Birds* (2009):** A self-aware wink (`#subtlereference`) to the dominant iOS App Store hit at the time of *S:S&SEP*'s 2011 iPad/iPhone debut. | Translate literally (`angry bird`) so it describes the scowling stone bird statues while keeping the wink obvious. |
| `D308`, `D311–D319` | `...upload The Megatome to the whirling infinite atop Mingi Taw.` | **Cloud Computing (`upload` to *The Kingdom of the Cloud*):** Earlier in `D005`, Mingi Taw is called *The Kingdom of the Cloud*. `"Uploading"` the Megatome to the summit is a deliberate tech-anachronism punning on uploading data to `"the Cloud"`. | Use the modern digital verb for *uploading to the cloud* rather than a physical verb like `"carry"` so the Cloud pun lands. |
| `D675` (`CREDITS`) | `S:S&S EP is a link to the past.` | ***The Legend of Zelda: A Link to the Past* (SNES, 1991):** One of the game's primary design inspirations, playing on the double meaning of *link* (connection vs. Nintendo's hero Link). | Capitalizing `'Link'` in single quotes preserves the *Zelda* tribute in languages where the noun for `"connection"` wouldn't otherwise evoke the character Link. |
| `D683` (`CREDITS`) | `S:S&S EP was originally going to be called 'Poopsock'. This is actually true.` | **`"Poopsock"` (MMORPG slang):** Early-2000s gaming slang for playing a game so obsessively that one refuses to leave the computer even to use the bathroom. | Keep `'Poopsock'` untranslated as the historical working title. |

### 4. Literature, Philosophy, Politics & Folklore

| Row & ID | English Source | Cultural Reference & Context | Localization Advice |
|---|---|---|---|
| `D101–D102` (`INFO_UNWELLWELL`, `INFO_WELLNESS`) | `The well seemed unwell. #unwell #well` / `All's well that ends well. #unwell #well #wellness` | **William Shakespeare's *All's Well That Ends Well* (c. 1604):** Preceded by a homophonic pun on *well* (water well) and *unwell* (sick). | Since the water-well/good-health homophony rarely exists in other languages, use a sonic rhyme/pun in `D101` and the canonical Shakespearean proverb in `D102`. |
| `D234` (`ARCHETYPE_MUSHROOMHINT`) | `It has even been asserted that divinatory mushrooms may have played a significant role in the development of the human psyche.` | **Terence McKenna's *"Stoned Ape" Hypothesis* (*Food of the Gods*, 1992):** The countercultural theory that psilocybin mushrooms catalyzed human language and self-reflection. | Maintain the pseudo-academic, tentative register (`It has even been asserted... may have played`). |
| `D283` (`ARCHETYPE_GOLDMASTERINTRO`) | `Confused? Excellent. Keep calm & carry on.` | **1939 British Wartime Poster (*"Keep Calm and Carry On"*):** Ubiquitous British motivational slogan/meme pivoting away from The Archetype's usual arcane diction. | Either reference the *Keep Calm* slogan or adapt with an equally iconic, good-natured comedic catchphrase about staying calm in your target culture. |
| `D372–D373`, `D383` (`GCLUE_*`) | `There are two types of unknowns - the known unknowns & the unknown unknowns.` / `There are also unknown nouns...` | **Donald Rumsfeld's February 12, 2002 Pentagon Briefing:** Famous epistemological tongue-twister about *"known unknowns"* and *"unknown unknowns"*, followed by a pun on *unknowns / unknown nouns*. | Use the recognized philosophical/political translation of Rumsfeld's *"known unknowns"* in your language and link `D372` lexically or phonically back to it. |
| `D599` (`CREDITS`) | `Executive producer, hero of the people, leadership & strategery by Nathan Vella...` | **`"Strategery"` (*Saturday Night Live*, 2000):** Mock-presidential malapropism coined by Will Ferrell impersonating George W. Bush in a 2000 *SNL* debate sketch. | Coin a playful portmanteau on *strategy* to preserve the humorous neologism. |
| `D674` (`CREDITS`) | `...the mythopoetic psychocosmology of Robert E. Howard's sword and sorcery stories...` | **Robert E. Howard (1906–1936):** Pulp-fantasy pioneer who created *Conan the Cimmerian* and founded the *Sword and Sorcery* genre (whose prehistoric Hyborian Age draws directly on historical Cimmeria and Scythia). | Use the established literary name of the *Sword & Sorcery* subgenre in your language. |
| `D678` (`CREDITS`) | `S:S&S EP obliquely references Carl G. Jung & his fascinating ""Red Book"" all over the damn place.` | **Carl G. Jung's *The Red Book* (*Liber Novus*, published 2009):** Jung's illuminated manuscript of active imagination, archetypes, and dream-walking, which directly inspired **The Archetype** and the crimson **Megatome**. | Use the published title of Jung's *Liber Novus* in your language. |

---

## Version History

- **v1.0–v1.2** (2024) — Initial glossary creation, post-correction standards, and foundational grammar guidelines.
- **v1.3** (2026) — Harmonized cross-lingual standards and purged obsolete prototype rules following comprehensive in-game review.
- **v1.4** (2026) — Added Technical, UI & Engine Constraints (LQA Reference) documenting HUD collisions (`HOLD_SHIELD_TO_HEAL`, `QUIT`), `DIGIT_STRING`, multi-platform key superset, `ARCHETYPE_TREEHINT` cross-platform camera mechanics, `ARCHETYPE_GROTTOPARADOX`, `SCYTHIAN_FOUNDATION`, and bitmap font quote rules.
- **v1.5** (2026) — Added comprehensive Cross-Language Guide of Cultural References, Pop-Culture Homages & Literary Allusions.
- **v1.6–v1.7** (2026) — Addressed formal LQA/MQM audit feedback: documented official Capybara Games rows 230–236 with retro-hardware (iOS 4 / iPod Touch) binary schema verification, sensitivity controls taxonomy, `GO_HOME` vs. `QUIT`/`EXIT` hierarchies, `SPANISH_SPECIAL` glyph registration (Row 167), proportional-font pixel heuristic, telepathic ghost-quote lore facts, and clean separation of technical engine constraints from creative editorial decisions.
- **v1.8–v1.9** (2026) — Completed comprehensive MQM/LQA audit passes for `es-419` and `pt-BR` (*see detailed changelogs in [`spanish/readme.md`](spanish/readme.md#version-history) and [`portuguese/readme.md`](portuguese/readme.md#version-history)*).
- **v2.0** (2026) — Refactored documentation architecture: split language-specific glossaries, grammar, dialect rules, and localized LQA notes into [`spanish/readme.md`](spanish/readme.md) and [`portuguese/readme.md`](portuguese/readme.md), leaving this document strictly as the global cross-language guide and technical reference.

---

## Contributors & Acknowledgments

- **Original game text:** Superbrothers Inc., Capy Games, Jim Guthrie
- **Spanish & Portuguese localizations & LQA documentation:** [cesardeg](https://github.com/cesardeg)

For questions, corrections, or additions to this guide, please submit issues to the repository.

---

## License

This localization documentation is provided as reference material for the *Superbrothers: Sword & Sworcery EP* localization project. Usage rights follow the game's original licensing terms.
