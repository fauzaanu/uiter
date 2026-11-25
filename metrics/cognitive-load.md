# Cognitive Load

> Cognitive Load measures how much mental effort the screen demands by limiting the number of decisions and information items a user must hold and process at the same time.

## What it measures

- Count of distinct items a user must hold in mind to act: visible options, labels, values and rules that compete for attention in one view.
- Count of simultaneous decisions the screen asks for before the user can make progress (primary actions, required fields, unrelated choices).
- Whether information is grouped into a small number of chunks that a user can scan as units, rather than presented as a flat list.
- Whether advanced or rarely needed controls are hidden until requested, or shown by default.
- Whether the user must remember values, states or steps from elsewhere on the screen or from earlier steps to complete the task.

## Research basis

- Working memory holds a small number of chunks. Cowan's review argues for a central capacity of about 3 to 5 chunks in adults, revising Miller's estimate of about seven. Anchor the rubric to 3 to 5 chunks. Cowan (2001), Behavioral and Brain Sciences, https://pubmed.ncbi.nlm.nih.gov/11515286/ (full text: https://memory.psych.missouri.edu/assets/doc/articles/2001/cowan-bbs-2001.pdf).
- Cognitive load theory distinguishes load imposed by the task from load imposed by how material is presented; load that does not serve understanding is extraneous and is the part a designer can reduce. Sweller (1988), "Cognitive Load During Problem Solving: Effects on Learning," Cognitive Science 12(2), 257-285. The primary paper was not read directly; the description comes from secondary summaries. See Open questions.
- NN/g treats cognitive load as unavoidable and recommends removing extraneous load so that remaining capacity goes to essential decisions, including chunking content. Nielsen Norman Group, "Minimize Cognitive Load," https://www.nngroup.com/articles/minimize-cognitive-load/ (only excerpts were retrieved).
- Decision time increases with the number of choices, roughly logarithmically (Hick-Hyman law). The cited sources also note that the law is weak for structured sets of alternatives, so it supports limiting options but not a fixed number. Hick (1952) and Hyman (1953), summarized at https://en.wikipedia.org/wiki/Hick%27s_law (secondary source; primary papers not retrieved).
- Cognitive load measurement in usability work is usually done with questionnaires such as NASA-TLX, which has been revised to map onto load types, and a 2024 extraneous-load instrument for mobile learning interfaces. Neither is a validated screen-level heuristic. Review: https://arxiv.org/abs/2402.11820; Heliyon (2024) via https://doaj.org/article/e84ec60dc0564af488c0c05ded27d741.

## Scoring method

1. Open the screen at the most common viewport and in its default state. Note the primary task it supports.
2. List every interactive control and every block of text or data visible without scrolling or interaction. Ignore decorative elements.
3. Count simultaneous decisions: distinct choices the user must make before the primary action is available (fields to fill, options to choose between, required settings).
4. Group the items into chunks by proximity, heading or container. Count the chunks and the items in the largest chunk.
5. Mark each item as essential to the task or extraneous (not needed for this task at this moment). Count the extraneous items.
6. Check for memory dependence: note any value, state or instruction the user must recall from another screen or step.
7. Trigger the main disclosure controls (menus, "more", advanced sections) once. Note whether advanced content was hidden by default.
8. Record: decisions (n), chunks (n), items in largest chunk (n), extraneous items (n), memory dependences (n), and disclosure yes or no. Apply the rubric.

## Scoring rubric

Scale: 0 = severe failure, 5 = exemplary.

- **0**: Dozens of controls and data points visible with no grouping; the primary action is unclear; the user must hold many values in mind to proceed.
- **1**: Items are visible in one undifferentiated mass (more than about 9 items in one group); several unrelated decisions compete; advanced options are shown by default.
- **2**: Some grouping exists, but the largest group exceeds about 7 items or the screen asks for more than 5 simultaneous decisions; extraneous items are common.
- **3**: Items are grouped into roughly 3 to 7 chunks; the largest group is about 5 to 7 items; a few extraneous items or one memory dependence remain.
- **4**: Essential decisions are about 3 to 5 at a time; chunks fit the 3 to 5 range in Cowan's estimate; advanced content is disclosed; at most one memory dependence.
- **5**: Only the decisions the current task needs are visible, in no more than about 4 chunks; no extraneous items; advanced content is disclosed on request; no memory dependence; the path to the next step is evident without reading everything.

## Automated checks (optional)

None reliable; manual review only. Automated tools can count DOM nodes or interactive elements, but they cannot tell which items are essential to the task, so they cannot produce a load score.

## Common failure patterns

- Settings and configuration pages that show every option at once, with no default or progressive disclosure (Cowan's limit is exceeded in one view).
- Forms that ask for several unrelated decisions on one screen, so the user cannot tell which one matters first.
- Dense dashboards where the primary metric competes with many equally weighted secondary values.
- Wizards or screens that require users to remember a value from an earlier step rather than showing it in context.
- Long, unbroken lists of options with no grouping, which raise decision time in the Hick-Hyman pattern.

## Sources

- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. Behavioral and Brain Sciences, 24(1). https://pubmed.ncbi.nlm.nih.gov/11515286/
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257-285. (DOI unconfirmed; see Open questions.)
- Nielsen Norman Group. Minimize Cognitive Load. https://www.nngroup.com/articles/minimize-cognitive-load/
- Hick-Hyman law (secondary summary). https://en.wikipedia.org/wiki/Hick%27s_law
- Cognitive load measurement review (2024). arXiv:2402.11820. https://arxiv.org/abs/2402.11820
- Extraneous cognitive load instrument for mobile learning UI (2024). Heliyon. https://doaj.org/article/e84ec60dc0564af488c0c05ded27d741

## Open questions

- The Sweller 1988 DOI differs between sources (10.1207/s15516709cog1202_4 and 10.1016/0364-0213(88)90023-7). Confirm before citing.
- The Hick-Hyman primary papers (Hick 1952, Hyman 1953) were not read directly. The sources also disagree on how far the law applies to structured menus.
- The chunk thresholds (3 to 5 chunks; largest group of 7) come from Cowan's estimate for memory of unrelated items, not from studies of screens. Mapping them to UI chunks is a judgment call.
- The "about 9 items" and "more than 5 decisions" breakpoints in the rubric are judgment calls, not research-backed numbers.
- NN/g's full article was not retrieved; only excerpts. Its specific tips should be checked before relying on them.
- No validated screen-level cognitive load heuristic was found. The scoring method is a manual proxy and has not been validated against user measures.
