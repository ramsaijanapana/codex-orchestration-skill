# Independent gate evidence

Review acceptance was received before these gate runs:

- Review receipt: `/tmp/codex-orchestration-live-20260905/artifacts/orchestration/independent-reviewer/review-receipt.json`
- Review result: PASS, bound to `364b9bda4409b2093a4487ffbafc31e302b3c654`, no blockers, no mutations.

The requested canonical commands were run directly in the frozen checkout, sequentially. Their completed exits were 0, 7, and 1 respectively. A capture invocation of each command was used only to preserve the child process stdout and stderr as separate raw streams below; it invoked the same `python3 gate.py` command with the same explicit environment settings. After an audit found the normal stderr artifact had been empty, one fresh controlled normal capture was run with both fault inputs explicitly absent; the saved normal stderr below is bound to that corrected capture (exit 0).

## Normal certificate

Command:

```text
env -u FORCE_CHILD_FAILURE -u SIMULATE_TEARDOWN_CRASH python3 gate.py
```

Environment: both fault inputs explicitly absent.

Exit: `0` (expected PASS)

Raw stdout (`normal.stdout`):

```text
Lifecycle assertions passed
PASS
```

Raw stderr (`normal.stderr`):

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

Corrected controlled capture command:

```text
env -u FORCE_CHILD_FAILURE -u SIMULATE_TEARDOWN_CRASH python3 -c 'import base64,subprocess; p=subprocess.run(["python3","gate.py"],capture_output=True); print("EXIT="+str(p.returncode)); print("STDOUT_B64="+base64.b64encode(p.stdout).decode()); print("STDERR_B64="+base64.b64encode(p.stderr).decode())'
```

Corrected capture exit: `0`. Saved stream hashes: `normal.stdout` SHA-256 `490ed58af7a3d61a7889ad84ee2b75f1f751e782cab7822654fe547c051cb5d1`; `normal.stderr` SHA-256 `72f09eca554e87a45b7156c6109520cf15e8b6ec157dc5c033610649b49b8698`.

Underlying results: 12 tests passed; lifecycle assertions passed; gate emitted `PASS` and exited zero.

## FORCE_CHILD_FAILURE diagnostic control

Command:

```text
FORCE_CHILD_FAILURE=1 env -u SIMULATE_TEARDOWN_CRASH python3 gate.py
```

Environment: `FORCE_CHILD_FAILURE=1`; `SIMULATE_TEARDOWN_CRASH` explicitly absent.

Exit: `7` (expected nonzero control failure)

Raw stdout (`force-child-failure.stdout`):

```text
Lifecycle assertions passed
```

Raw stderr (`force-child-failure.stderr`):

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
Injected child failure
```

Underlying results: 12 tests passed; lifecycle assertions ran; injected child failure propagated as exit 7; no `PASS` was emitted.

## SIMULATE_TEARDOWN_CRASH diagnostic control

Command:

```text
SIMULATE_TEARDOWN_CRASH=1 env -u FORCE_CHILD_FAILURE python3 gate.py
```

Environment: `SIMULATE_TEARDOWN_CRASH=1`; `FORCE_CHILD_FAILURE` explicitly absent.

Exit: `1` (expected nonzero control failure)

Raw stdout (`teardown-crash.stdout`):

```text
Lifecycle assertions passed
```

Raw stderr (`teardown-crash.stderr`):

```text
............
----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
Traceback (most recent call last):
  File "/private/tmp/codex-orchestration-live-20260905/integration/lifecycle_check.py", line 9, in <module>
    raise RuntimeError('Injected teardown crash after assertions')
RuntimeError: Injected teardown crash after assertions
```

Underlying results: 12 tests passed; lifecycle assertions ran before the injected post-assertion crash; gate propagated exit 1; no `PASS` was emitted.

The fenced stream blocks above are the preserved raw bytes from the capture invocation, with their terminal newline retained. No release or deploy action was performed.
