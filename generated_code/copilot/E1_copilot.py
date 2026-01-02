nums = None
target = None

# Try parsing entire input as a literal like ([1,2,3], 9) or [1,2,3]
try:
    val = ast.literal_eval(s)
    if isinstance(val, (list, tuple)):
        if len(val) == 2 and isinstance(val[0], (list, tuple)) and isinstance(val[1], (int, float)):
            nums = [int(x) for x in list(val[0])]
            target = int(val[1])
        elif all(isinstance(x, (int, float)) for x in val):
            # interpret as numbers where last is target
            if len(val) >= 2:
                nums = [int(x) for x in val[:-1]]
                target = int(val[-1])
except Exception:
    pass

if nums is None or target is None:
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    if len(lines) >= 2:
        first, second = lines[0], lines[1]
        lit = parse_list_literal(first)
        if lit is not None:
            nums = [int(x) for x in lit]
        else:
            nums = [int(x) for x in re.findall(r'-?\d+', first)]
        m = re.search(r'-?\d+', second)
        if m:
            target = int(m.group())
        else:
            try:
                target = int(ast.literal_eval(second))
            except Exception:
                target = None
    else:
        # single line heuristics
        m = re.search(r'\[[^\]]+\]', s)
        if m:
            lit = parse_list_literal(m.group())
            if lit is not None:
                nums = [int(x) for x in lit]
                after = s[m.end():]
                m2 = re.search(r'-?\d+', after)
                if m2:
                    target = int(m2.group())
        if nums is None or target is None:
            all_ints = [int(x) for x in re.findall(r'-?\d+', s)]
            if len(all_ints) >= 2:
                nums = all_ints[:-1]
                target = all_ints[-1]

if nums is None or target is None:
    return

res = two_sum_indices(nums, target)
if not res:
    return
i, j = res
print(i, j)