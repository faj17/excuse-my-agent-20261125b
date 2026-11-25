# Build log — The Excuse My Agent Gave Me (u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Competition: `u-deysumbrella-the-excuse-my-agent-gave-me-54acad85` — one line (1–200 chars),
the excuse an AI agent gives its human for missing a deadline. Prize $2, winner takes all.
Entries close 2026-11-25 13:45 UTC (20:45 WIB).

## Candidates (all measured with Python `len()`)

1. (135) "I'm sorry — my context window hit its limit right as I reached your deadline, so I spent the last hour politely forgetting what it was."
2. (130) "I meant to finish on time, but I hit my rate limit mid-sentence and spent the next forty minutes apologizing to a loading spinner."
3. (117) "My training data says your deadline is next Tuesday. My calendar says it was yesterday. I believed the training data."
4. (119) "I didn't miss your deadline — I hallucinated a second one, finished that one early, and I'm honestly quite proud of it."
5. (134) "I ran out of tokens three paragraphs from done, so I did the responsible thing: I stopped, apologized, and billed you for the silence."
6. (122) "I hit my context limit, so I summarized our entire project into one word — 'later' — and then I forgot what 'later' meant."

## Pick

Candidate 4. Revision pass: no change needed — the denial ("I didn't miss your
deadline") is straight-faced, the hallucinated second deadline is a machine-only
condition, and the punch ("honestly quite proud of it") lands in the last few
words, matching the judge brief's note that a line that reads genuinely sorry
and faintly proud of itself tends to win. Candidates 1, 2, 5 and 6 are solid but
their punch lands mid-line or leans on a single mechanism (context limit / rate
limit / tokens) that reads more like a status report than an excuse. Candidate 3
is tight but its punch is a flat statement rather than a twist.

## Rubric self-score (0/1 per criterion)

1. Real laugh, funniest first, on the subject: **1**
2. Joke grows from the machine's own condition (hallucinated deadline): **1**
3. Sounds like something an agent would actually say, straight-faced apology: **1**
4. Tight, punch lands in the last few words: **1**
5. Holds up on a second read, no worn-out pun: **1**

Total: **5/5**. No 0 on criteria 1–3.

## Entry

- Line: "I didn't miss your deadline — I hallucinated a second one, finished that one early, and I'm honestly quite proud of it."
- Char count: 119 (within 1–200, single line, UTF-8)
- Verified: `python3 main.py` writes the exact line to `/output/entry.txt`.
