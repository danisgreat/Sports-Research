# Post-checkout byte verification

The main release is 294aeb7af050d51ff1986d01ec17fe5c66aac8c4. Its initial main
checkout differed from CODE_TESTED.csv only in ml/tests/test_timing_v3.py line
endings (2,835 LF bytes versus the tested 2,883 CRLF bytes). Normalized Python
content was identical. The follow-up commit adds a raw-byte Git attribute for
that legacy test and restores the exact tested bytes; no Python logic changes.

After restoration all 152 tested Python files and all 2,228 protected historical
files match their byte manifests. The 10 TIMING-v3 tests passed again on main in
6.86 seconds. The preceding .gitattributes is retained byte-exact in the archive's
POST_CHECKOUT_GITATTRIBUTES.txt and bound by POST_CHECKOUT_ORIGINAL.csv. Earlier
validation reports and their disclosed dependency-map failure/fix remain unchanged.

The final response reports the verified published main SHA after this follow-up
and mirror synchronization. No full-suite result is re-labelled: see VALIDATION.md
and TEST_RUNS.csv for the actual full-run and corrected documentation check results.
