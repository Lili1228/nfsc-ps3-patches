@echo off
setlocal
set PATH=%PATH%;"%~dp0bin\"

python bin\patch_ppc_elf.py bin\EBOOT.ELF EBOOT-patched.elf patches.txt 0x10000
if exist patches_data.txt ( 
    python bin\patch_ppc_elf.py EBOOT-patched.elf EBOOT-patched-data.elf patches_data.txt 0xF6C0000
    
    if exist EBOOT-patched-data.elf (
        del /Q EBOOT-patched.elf
        ren EBOOT-patched-data.elf EBOOT-patched.elf
    )
)

make_fself EBOOT-patched.ELF EBOOT-patched.BIN

endlocal