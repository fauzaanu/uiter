# Recognition over Recall

> Measures whether users can see options and cues on screen rather than having to remember them from elsewhere in the product or from earlier steps.

## What it measures

- Whether the commands, options, and destinations needed for a task are visible on the screen, not hidden behind a memorized shortcut or a remembered path.
- Whether the current state of a flow (selected filters, entered values, active mode, step in a sequence) is shown rather than expected to be remembered.
- Whether labels carry their own meaning, so a user does not need to recall what an abbreviation, icon, or code refers to.
- Whether the user must carry information from one screen or step to another (IDs, values, names) when the interface could display or prefill it.
- Whether help, hints, and format examples appear in context at the point of need, not only in a separate tutorial or manual.

## Research basis

- Recall involves fewer retrieval cues than recognition, so recognition is the easier memory task. Claim: menus are the classic recognition-based interface. Source: Nielsen Norman Group, "Recognition and Recall," https://www.nngroup.com/articles/recognition-and-recall/
- Heuristic 6 asks designers to minimize memory load by making objects, actions, and options visible, and to offer help in context rather than a tutorial to memorize. Source: Nielsen Norman Group, "10 Usability Heuristics for User Interface Design," https://www.nngroup.com/articles/ten-usability-heuristics/
- The same NN/g material illustrates the difference with prompted versus unprompted questions: confirming "Is Lisbon the capital of Portugal?" is easier than answering "What is the capital of Portugal?" Source: Nielsen Norman Group, "Usability Heuristic 6: Recognition vs. Recall in User Interfaces" (video), https://www.nngroup.com/videos/recognition-vs-recall/
- Recall of menu structure depends heavily on study conditions. In a study of memory for menus, subjects who studied a command sequence recalled menu terms best, while other groups relied heavily on their memory of the menu tree. Source: Norman, Schwartz and Shneiderman (1984), "Memory for Menus: Effects of Study Mode," https://lccd.umiacs.umd.edu/node/17294. Only the abstract-level summary was reviewed.
- A transitional interface that exposes menu-style options alongside commands produced higher performance and higher perceived usability for inexperienced users than a command-only interface. Source: Badre and Morris, "The Effects of Manipulating Recognition Variables on the Transition from Menus to Commands," https://repository.gatech.edu/entities/publication/5029ea30-bf1e-4f6c-8d44-93d24eca4d44. Only the summary was reviewed.
- Display-based interaction rests on the assumption that recognition rather than recall of commands and interface objects drives performance, and the number of distracting objects affects how quickly the right object is found. Source: Franzke, CHI '95 Proceedings, https://chi1995.chistatic.hosting.acm.org/proceedings/papers/mf_bdy.htm. Only the abstract-level summary was reviewed.

## Scoring method

1. Pick one common task the screen supports (for example, "change the delivery address" or "export a report") and write down every step a user would take to complete it.
2. For each step, list what the user must know that is not visible on the current screen: a command name, a menu location, a previously entered value, an ID, a format, or the meaning of an icon.
3. Count those hidden items. Note each one as a recall demand.
4. Check the state indicators: confirm that active filters, selected items, current mode, and progress through the flow are visible without the user having to remember them.
5. Check labels and icons: confirm each icon has a text label or a tooltip where its meaning is not standard, and that abbreviations are expanded or explained.
6. Check in-context support: confirm that format hints, examples, and help appear next to the field or action that needs them.
7. Check carry-over: confirm that values from earlier steps are displayed or prefilled where the next step needs them.
8. Record the number of recall demands per task, the number of steps with state visibility problems, and a short note for each. Score the screen against the rubric.

## Scoring rubric

- **0:** Core tasks cannot be completed without memorized commands, paths, or codes. No state is visible. Users must carry values across screens by hand.
- **1:** Most tasks need recall of a hidden command, path, or code. Some state is visible, but key state (mode, filters, selections) is not.
- **2:** Primary actions are visible, but several secondary tasks rely on memorized shortcuts, unlabeled icons, or values carried from other screens.
- **3:** Primary and most secondary actions are visible and labeled. State is shown for the main flow. A few recall demands remain, such as an unexplained icon or a value that is not prefilled.
- **4:** All common tasks are completable from what is on screen. Icons are labeled or have tooltips where meaning is not standard. Values carry over between steps. Help appears in context.
- **5:** Every task is discoverable from the screen. Recent or relevant options are surfaced without a search. State is always visible. Nothing needs to be remembered between steps, and help is given at the point of need.

Numeric thresholds: none reliable from the sources reviewed. The anchors above are structural and count-based, so the scale is a judgment call (see Open questions).

## Automated checks (optional)

None reliable; manual review only. Automated tools can detect missing accessible names on icon buttons, but they cannot tell whether a visible option is discoverable or whether state is understood without memory.

## Common failure patterns

- Commands are available only through keyboard shortcuts or hidden menus, so users must recall them. Heuristic 6 and the recognition-over-recall principle both argue against this (NN/g, https://www.nngroup.com/articles/ten-usability-heuristics/).
- Multi-step forms or wizards do not show earlier entries, so users must remember values typed on previous screens.
- Icon-only controls with non-standard meanings force users to guess or remember what each one does (NN/g, https://www.nngroup.com/articles/recognition-and-recall/).
- Active filters, modes, or selections are not displayed, so users cannot tell what state the screen is in.
- Help lives in a separate manual or tutorial, not next to the field or action that needs it (NN/g, https://www.nngroup.com/articles/ten-usability-heuristics/).
- Identifiers such as order numbers or codes are shown on one screen and required on another with no link or copy aid.

## Sources

1. Nielsen Norman Group. "Recognition and Recall." https://www.nngroup.com/articles/recognition-and-recall/
2. Nielsen Norman Group. "10 Usability Heuristics for User Interface Design" (Heuristic 6). https://www.nngroup.com/articles/ten-usability-heuristics/
3. Nielsen Norman Group. "Usability Heuristic 6: Recognition vs. Recall in User Interfaces" (video). https://www.nngroup.com/videos/recognition-vs-recall/
4. Norman, D. A., Schwartz, S. and Shneiderman, B. (1984). "Memory for Menus: Effects of Study Mode." https://lccd.umiacs.umd.edu/node/17294
5. Badre, A. and Morris, J. "The Effects of Manipulating Recognition Variables on the Transition from Menus to Commands." Georgia Tech repository. https://repository.gatech.edu/entities/publication/5029ea30-bf1e-4f6c-8d44-93d24eca4d44
6. Franzke, M. "CHI '95 Proceedings" (display-based interaction paper). https://chi1995.chistatic.hosting.acm.org/proceedings/papers/mf_bdy.htm

## Open questions

- The Norman, Schwartz and Shneiderman (1984) and Badre and Morris entries were taken from search summaries and repository listings. Full text was not reviewed, so effect sizes, methods, and the exact year and author list for Badre and Morris are unverified.
- The Franzke CHI '95 entry is known only from a search excerpt. Its exact title and author list should be confirmed against the ACM Digital Library before formal citation.
- The research establishes the principle that recognition is easier than recall. It does not supply numeric thresholds for "how many recall demands" are acceptable, so the 0 to 5 anchors are a judgment call.
- WCAG 2.2 Success Criterion 3.3.7 (Redundant Entry) addresses re-entering previously provided information. It was not retrieved in this session and should be verified before citing.
- Whether recognition-based designs always outperform recall-based ones for expert users is not settled by the sources reviewed. The Badre and Morris finding concerns inexperienced users.
