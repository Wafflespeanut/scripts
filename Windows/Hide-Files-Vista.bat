cls
@ECHO OFF
if EXIST "Stealth.{ED7BA470-8E54-465E-825C-99712043E01C}" goto GET
if NOT EXIST Cache goto MAKE
:HIDE
ren Cache "Stealth.{ED7BA470-8E54-465E-825C-99712043E01C}"
attrib +h +s "Stealth.{ED7BA470-8E54-465E-825C-99712043E01C}"
goto END
:GET
attrib -h -s "Stealth.{ED7BA470-8E54-465E-825C-99712043E01C}"
ren "Stealth.{ED7BA470-8E54-465E-825C-99712043E01C}" Cache
goto END
:MAKE
md Cache
goto END
:END