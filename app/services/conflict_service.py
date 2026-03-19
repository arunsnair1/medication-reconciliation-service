def detect_conflicts(old_meds, new_meds):
    conflicts = []

    old_map = {m["name"]: m for m in old_meds}

    for med in new_meds:
        name = med["name"]

        if name in old_map:
            old = old_map[name]

            # case 1: dose mismatch
            if old["dose"] != med["dose"]:
                conflicts.append({
                    "type": "DOSE_MISMATCH",
                    "drug": name,
                    "old_dose": old["dose"],
                    "new_dose": med["dose"]
                })

            # case 2: status mismatch
            if old["status"] != med["status"]:
                conflicts.append({
                    "type": "STATUS_CONFLICT",
                    "drug": name,
                    "old_status": old["status"],
                    "new_status": med["status"]
                })

    return conflicts