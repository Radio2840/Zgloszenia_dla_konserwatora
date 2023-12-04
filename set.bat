@echo off
set py="%cd:~0,3%progreming\_ProgramFiles\python\python.exe"
doskey py = %py% $*
doskey python = %py% $*
echo python path: %py%

set node="%cd:~0,3%progreming\_ProgramFiles\nodejs\node.exe"
doskey node = %node% $*
doskey n = %node% $*
echo nodejs path: %node%


set npm="%cd:~0,3%progreming\_ProgramFiles\nodejs\npm.cmd"
doskey npm = %npm% $*
echo npm path: %npm%