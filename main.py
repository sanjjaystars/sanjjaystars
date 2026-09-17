from datetime import datetime

import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO     = "./fonts/vtks-blocketo.regular.ttf"
FONT_FILE_BITMAP   = "./fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "./fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA     = "./fonts/Inversionz.otf"

USERNAME    = "sanjjaystars"
EMAIL       = "sanjjay.stars@gmail.com"
LINKEDIN    = "sanjjayaroumougam"
OS_INFO     = "Arch/Fedora Linux, MacOS"
HOST        = "SMVEC"
KERNEL      = "CS Engineering & Business System #CSBS"
IDE         = "nano, neovim, VSCode"
BIRTH       = (20, 11, 2007)   # day, month, year
TIMEZONE    = "Asia/Kolkata"


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    # ── Phase 1: BIOS boot screen ─────────────────────────────────────────────
    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo(TIMEZONE)).strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, \x1b[31mSanjjaystars Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):  # 64K Memory Test
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    # ── Phase 2: Boot sequence + GIF OS logo scramble ─────────────────────────
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)
    t.set_font(FONT_FILE_LOGO, 66)
    os_logo_text = "GIF OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    # ── Phase 3: Login screen ─────────────────────────────────────────────────
    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text(f"\x1b[93mGIF OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text(USERNAME, 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo(TIMEZONE)).strftime("%a %b %d %I:%M:%S %p %Z %Y")
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # ── Phase 4: Prompt + clear command with syntax highlight ─────────────────
    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    # ── Phase 5: Fetch GitHub stats & build info screen ───────────────────────
    git_stats = gifos.utils.fetch_github_stats(USERNAME)
    user_age  = gifos.utils.calc_age(*BIRTH)
    top_langs = [lang[0] for lang in git_stats.languages_sorted]

    t.clear_frame()
    user_details_lines = f"""
    \x1b[30;101m{USERNAME}@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93m{OS_INFO}\x1b[0m
    \x1b[96mHost:   \x1b[93m{HOST}\x1b[0m
    \x1b[96mKernel: \x1b[93m{KERNEL}\x1b[0m
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    \x1b[96mIDE:    \x1b[93m{IDE}\x1b[0m
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93m{EMAIL}\x1b[0m
    \x1b[96mLinkedIn:   \x1b[93m{LINKEDIN}\x1b[0m
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_stats.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_stats.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_stats.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_stats.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_stats.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_stats.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_langs[:5])}\x1b[0m
    """

    # ── Phase 6: fetch.sh command with syntax highlight ───────────────────────
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text(f"\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(f" -u {USERNAME}", 1, contin=True)

    # ── Phase 7: ASCII Mona cat + info panel side-by-side ────────────────────
    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# Have a nice day kind stranger :D Thanks for stopping by!",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=120, contin=True)

    # ── Render GIF & write README ─────────────────────────────────────────────
    t.gen_gif()

    readme_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="GIFOS" src="output.gif">
</picture>

<sub><i>Generated automatically using <a href="https://github.com/sanjjaystars/github-readme-terminal">sanjjaystars/github-readme-terminal</a> on {time_now}</i></sub>
</div>

<br />

### Languages · frameworks · tools

<div align="center">
  <!-- Update this row to match the technologies you use. -->
  <img src="https://skillicons.dev/icons?i=git,github,vscode,java,python,cpp,html,css,js&theme=dark" alt="Git, GitHub, VS Code, Java, Python, C++, HTML, CSS, and JavaScript" />
</div>

<br />
<div align="center">
  <img src="https://raw.githubusercontent.com/sanjjaystars/sanjjaystars/output/github-contribution-grid-snake-dark.svg" alt="Animated contribution snake" />
</div>

<hr />

<div align="center">
  <sub>Made with ☕ and consistency by <a href="https://github.com/sanjjaystars">Sanjjay</a></sub>
</div>

<hr />
"""
    with open("README.md", "w") as f:
        f.write(readme_content)
        print("INFO: README.md generated")


if __name__ == "__main__":
    main()
