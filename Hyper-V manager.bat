@ECHO OFF

:: Controllo permessi
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Success: Administrative permissions confirmed.
    goto admin
) else (
    echo Failure: Current permissions inadequate.
    ::pause >nul
    goto admin
    :: goto admin solo per debug
)

:admin
    echo 1 - Attivare Hyper-V
    echo 2 - Disattivare Hyper-V
    set /p scelta=
    if %scelta% == 1 (
        echo scelta 1
        goto fine
    )
    if %scelta% == 2 (
        echo scelta 2
        goto fine
    )

:fine
    pause
