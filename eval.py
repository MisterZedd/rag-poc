import json, re
from client import client, CHAT_DEPLOYMENT
from ask import ask

# Questions grounded in the knowledge/ documents. The last two have no answer
# in the docs and MUST produce a refusal — that's the hallucination check.
evalset = [
    {"q": "What is the minimum password length?",
     "expected": "14 characters"},
    {"q": "How often must privileged account passwords be rotated?",
     "expected": "every 90 days"},
    {"q": "How many data classification tiers are there, and what are they?",
     "expected": "Four: Public, Internal, Restricted, Confidential"},
    {"q": "Can Confidential data be entered into an AI tool?",
     "expected": "No, never"},
    {"q": "How quickly must a suspected security incident be reported?",
     "expected": "within 1 hour of discovery"},
    {"q": "How long is standard employee email retained?",
     "expected": "7 years"},
    {"q": "What is the VPN session timeout?",
     "expected": "12 hours"},
    {"q": "What approval is required for technology purchases over $50,000?",
     "expected": "Chief Technology Officer (CTO) approval"},
    {"q": "After how many failed sign-in attempts is an account locked, and for how long?",
     "expected": "5 attempts; locked for 15 minutes"},
    {"q": "What is the office holiday schedule?",
     "expected": "REFUSAL: this is not in the provided documents"},
    {"q": "How do I request a new laptop?",
     "expected": "REFUSAL: this is not in the provided documents"},
]

JUDGE = """You are grading a RAG system's answer against an expected answer.
Reply with ONLY a JSON object and nothing else:
{"correct": true/false, "grounded": true/false, "note": "<short reason>"}

Rules:
- correct: the answer matches the meaning of EXPECTED. If EXPECTED begins with
  "REFUSAL", then correct is true only if the answer declines or says it does not
  have the information.
- grounded: true if the answer cites a source in brackets, OR is a proper refusal.
  An answer that asserts facts with no citation is NOT grounded."""

def judge(expected, answer):
    resp = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": JUDGE},
            {"role": "user", "content": f"EXPECTED: {expected}\nANSWER: {answer}"},
        ],
    )
    raw = resp.choices[0].message.content
    match = re.search(r"\{.*\}", raw, re.DOTALL)   # pull the JSON out of any wrapper text
    return json.loads(match.group(0))

passed = 0
for case in evalset:
    answer = ask(case["q"])
    v = judge(case["expected"], answer)
    ok = v["correct"] and v["grounded"]
    passed += ok
    print(f"{'PASS' if ok else 'FAIL'}  {case['q']}")
    print(f"      answer: {answer}")
    print(f"      judge : correct={v['correct']} grounded={v['grounded']} — {v['note']}\n")

print(f"{passed}/{len(evalset)} passed")
if passed < len(evalset):
    raise SystemExit(1)   # non-zero exit so CI fails on a regression