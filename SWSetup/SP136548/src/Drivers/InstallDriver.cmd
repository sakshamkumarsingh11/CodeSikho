@echo off
CLS
setlocal enabledelayedexpansion

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "%1", "", "runas", 1 >> "%temp%\getadmin.vbs"

    wscript "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

echo **************************************************************
echo ***  Batch Install Realtek Wireless LAN Driver               
echo ***                                                            
echo ***  Please wait a moment	                  
echo=

if %PROCESSOR_ARCHITECTURE%==AMD64 (
    set WiFiDIR="C:\Program Files (x86)\Realtek\PCIE Wireless LAN"
    set DriverSrcPath="%~dp0RTWLANE_Driver\Win10X64"
    set DPInstPath="%~dp0RTWLANE_Driver\DPInst\X64"
)
if %PROCESSOR_ARCHITECTURE%==x86 (
    set WiFiDIR="C:\Program Files\Realtek\PCIE Wireless LAN"
    set DriverSrcPath="%~dp0RTWLANE_Driver\Win10X86"
    set DPInstPath="%~dp0RTWLANE_Driver\DPInst\X86"
)
set VersionPath="%~dp0RTWLANE_Driver\Version"
set var=%WiFiDIR:~1,-1%

set sourcePath="%TEMP%\Realtek\RTWLANE_Install"
if NOT exist %sourcePath% (mkdir %sourcePath%)
set logPath="%ProgramData%\HP\Logs\Realtek"
if NOT exist %logPath% (mkdir %logPath%)

xcopy /y "%~dp0U*" "%var%\" /s > nul
xcopy /y "%~dp0RTWLANE_Driver\Win10X64\*" "%var%\RTWLANE_Driver\Win10X64\" /s > nul
xcopy /y "%~dp0RTWLANE_Driver\Win10X86\*" "%var%\RTWLANE_Driver\Win10X86\" /s > nul
xcopy /y "%~dp0RTWLANE_Driver\DPInst\*" "%var%\RTWLANE_Driver\DPInst\" /s > nul

xcopy /y %VersionPath%\* "%var%\" /s /e > nul
xcopy /y %DriverSrcPath%\* %sourcePath%\ /s /e > nul
xcopy /y %DPInstPath%\* %sourcePath%\ /s /e > nul

set logfile=%logPath%\WiFiInst.log

echo ----- %date% %time% ----- Installation BEGIN > %logfile%

pnputil /add-driver %sourcePath%\netrtwlane601.inf /install >> %logfile%
pnputil /add-driver %sourcePath%\netrtwlane6.inf /install >> %logfile%
pnputil /add-driver %sourcePath%\netrtwlane.inf /install >> %logfile%
pnputil /add-driver %sourcePath%\netrtwlane02.inf /install >> %logfile%

set var=%sourcePath:~1,-1%

for /F "tokens=*" %%A in ('reg query "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}" /f "DEV_C822" /d /s 2^>nul ^| find /I "HKEY_LOCAL_MACHINE"') do (
echo 8822CE is %%A >> %logfile%
"%var%\devcon.exe" disable "@PCI\VEN_10EC&DEV_C822*" >> %logfile%
echo Parameter is [%1] >> %logfile%
if "%1"=="" reg add %%A /v HP_WA_Config /t REG_SZ /d "0" /f
if "%1"=="LOW" reg add %%A /v HP_WA_Config /t REG_SZ /d "1" /f
"%var%\devcon.exe" enable "@PCI\VEN_10EC&DEV_C822*" >> %logfile%
)

echo ----- %date% %time% ----- Installation END >> %logfile%
type %logfile%

echo=     
echo **************************************************************
echo ***  Driver Install Finished                                       
echo=

rem if exist %sourcePath% (rd /s/q %sourcePath%)
popd
