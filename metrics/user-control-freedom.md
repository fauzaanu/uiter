# User Control and Freedom

> Measures whether users can undo, cancel, back out of, and escape from actions and flows.

## What it measures
- Every multi-step flow (wizard, checkout, form, modal, drawer) has a visible way to leave: a labeled Cancel, Close, or Back control that does not require finishing the flow.
- Destructive or committing actions (delete, send, submit, bulk change) can be reversed through Undo, a restore option, or a recoverable state, or are preceded by a review step the user can back out of.
- Modal dialogs, overlays and menus can be dismissed by a visible control and by the Escape key.
- Pointer and drag interactions can be aborted before they commit (for example, releasing the pointer off the target, or dragging back to the origin).
- Users can return to the previous step or screen without losing entered data.

## Research basis
- Users often choose system functions by mistake and need a clearly marked "emergency exit" to leave an unwanted state without an extended dialogue; undo and redo support freedom to explore. Source: Nielsen Norman Group, "User Control and Freedom" (Jakob Nielsen's third heuristic), https://www.nngroup.com/articles/user-control-and-freedom/ ; and "Ten Usability Heuristics," https://www.nngroup.com/articles/ten-usability-heuristics/
- Undo and erase events are useful automatic indicators of usability problems. In a within-subjects lab study (reported as 35 participants) they revealed over 90% of the problems rated severe, several missed by self-report. Source: Akers, Simpson, Jeffries and Winograd, "Undo and Erase Events as Indicators of Usability Problems," CHI 2009, https://hci.stanford.edu/publications/paper.php?id=67 (figures taken from the search summary, not checked against the full text).
- In multi-user VR, participants used undo whenever it was available, and undo raised perceived success more than actual success. Source: "Just Undo It: Exploring Undo Mechanics in Multi-User Virtual Reality," arXiv 2403.11756 (reported at CHI 2024 in search results), https://arxiv.org/pdf/2403.11756
- Reversible submissions, checked input, or a review-and-confirm step are required for legal, financial, and user-data transactions, because people may mistype or mis-key. A confirmation step is not required for every routine save. Source: W3C, "Understanding SC 3.3.4 Error Prevention (Legal, Financial, Data)," WCAG 2.x, https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html
- Pointer activation should occur on the up-event so users can abort by moving off the target before release. Source: W3C, "Understanding SC 2.5.2 Pointer Cancellation" (WCAG 2.2), https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation

## Scoring method
1. Pick one screen or one flow (start to finish). List every state that can be entered: each step, each modal, each drawer, each destructive action.
2. For each entry point, check for a visible exit control (Cancel, Close, Back, or X) in the expected location. Record yes/no and the label text.
3. Open each modal or overlay and press Escape. Record whether it closes. Click outside and record the result; note it, but do not score it as a pass or fail on its own.
4. For each committing or destructive action, check whether it has (a) an Undo or restore path, (b) a review step before commit, or (c) a confirmation for irreversible loss. Record which one, or none.
5. Mid-flow, enter data, then use Back or Cancel. Confirm entered data survives Back and is discarded only on explicit Cancel. Record the result.
6. For drag or press interactions, start the action, move off the target, release. Confirm nothing commits. Record the result.
7. Count the checks passed out of the total applicable checks. Note any flow where the user is trapped (no visible exit and no Escape).

## Scoring rubric
- **0**: Severe failure. Users are trapped in a flow or modal with no visible exit. Destructive actions are irreversible with no confirmation.
- **1**: Most flows lack a visible exit or undo. Escape does not close overlays. Users must reload or restart to recover.
- **2**: Some flows have exits, but several committing actions are irreversible or have no cancel. Back loses entered data in at least one flow.
- **3**: Most flows have a visible Cancel/Close/Back. Most destructive actions have undo or confirmation. Minor gaps: one or two modals lack Escape, or one action lacks a reversal path.
- **4**: Every flow has a visible exit. Overlays close via control and Escape. Destructive and financial actions are reversible or reviewed. Data survives Back. Only cosmetic inconsistencies in labels or placement.
- **5**: Exemplary. Every check passes. Undo or restore is available for reversible actions. Cancel is consistently placed and labeled across the product. Pointer actions abort cleanly. No trapped states.

## Automated checks (optional)
None reliable; manual review only. Partial aid: a DOM script can list modals and check for a focusable close button and an Escape keydown handler, but it cannot judge whether an exit is discoverable, whether undo covers the right actions, or whether data survives Back.

## Common failure patterns
- Modals with no visible close control, so only users who know Escape can leave (ARIA dialog guidance expects both Escape and a visible control; Deque's modal rule reflects this).
- Multi-step wizards where Back clears entered data, forcing re-entry.
- Destructive deletes with neither undo nor confirmation, especially in bulk actions.
- Confirmation dialogs that offer only "OK" with no Cancel.
- Press-and-act controls that fire on pointer-down, so the user cannot abort by moving away (WCAG 2.2 SC 2.5.2).
- Undo that exists for some actions but silently excludes others, so users cannot predict what is reversible.

## Sources
1. Nielsen Norman Group. "User Control and Freedom." https://www.nngroup.com/articles/user-control-and-freedom/
2. Nielsen Norman Group. "Ten Usability Heuristics." https://www.nngroup.com/articles/ten-usability-heuristics/
3. Akers, D., Simpson, R., Jeffries, R., and Winograd, T. (2009). "Undo and Erase Events as Indicators of Usability Problems." CHI 2009. https://hci.stanford.edu/publications/paper.php?id=67
4. "Just Undo It: Exploring Undo Mechanics in Multi-User Virtual Reality." arXiv:2403.11756. https://arxiv.org/pdf/2403.11756
5. W3C. "Understanding SC 3.3.4 Error Prevention (Legal, Financial, Data)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html
6. W3C. "Understanding SC 2.5.2 Pointer Cancellation," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation

## Open questions
- The Akers 2009 figures (35 participants, over 90% of severe problems) come from a search summary; the full paper was not read. Verify before citing numbers.
- The "Just Undo It" paper's venue (CHI 2024) and participant count were reported in search snippets and were not verified against the ACM record.
- No controlled study was found on cancel or emergency-exit affordances specifically. The emergency-exit and cancel guidance rests on NN/g heuristic practice, not on an experiment.
- Light dismiss (clicking outside a modal) has no settled research answer; sources disagree. It is not scored here.
- Which actions must be undoable versus confirmed is a judgment call; the rubric's thresholds (for example, "most" destructive actions) are not research-derived numeric cutoffs.
- The Deque and ARIA modal guidance was seen only through secondary summaries; the ARIA Authoring Practices original was not fetched.
