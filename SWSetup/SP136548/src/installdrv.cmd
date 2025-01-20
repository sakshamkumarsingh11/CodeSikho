REM ========================================================
REM   Driver deliverable installation
REM 
REM   Template Version: V1.03b
REM ========================================================
set versiondrv=1.03b
set errcode=0
REM %Description of deliverable%
@ECHO OFF
REM ****************************************************
REM *      COMPONENT OWNER TO UPDATE (SW_TITLE)        *
REM ****************************************************
SET SW_TITLE=RealtekRT_P0117TB2
REM ****************************************************
set DriverPrefix=dchu_
REM MODIFY SET DRIVERPREFIX AS NEEDED
if not exist "%~dp0%driverprefix%" set DriverPrefix=driver

rem
rem Set up the log folder/file
rem
if defined FCC_LOG_FOLDER (
    SET "APP_LOG=%FCC_LOG_FOLDER%\%~n0.log"
    if not exist "%FCC_LOG_FOLDER%" md "%FCC_LOG_FOLDER%"
) else (
    SET "APP_LOG=c:\programdata\HP\logs\%SW_TITLE%.log"
    if not exist "c:\programdata\HP\logs" md "c:\programdata\HP\logs"
)

rem
rem No need to install driver here (online) during preinstall if it supports INF injection, and doesn't have NOINF.FLG
rem
if not exist "..\NOINF.FLG" if exist "c:\system.sav\tweaks" if exist "c:\system.sav\flags\Proteus.FLG" (
    echo ***INFO*** For Preinstall, we've already injected the driver offline --^> skip the installation here. >> "%APP_Log%"
    goto lbl_CommonOps 
)

ECHO ############################################################# >> %APP_LOG%
ECHO  [%DATE%]                                                     >> %APP_LOG%
ECHO  [%TIME%] Beginning of the %~nx0                              >> %APP_LOG%
ECHO ############################################################# >> %APP_LOG%

set "ExtensionGuid={e2f84ce7-8efa-411c-aa69-97454ca4cb57}"
set "SoftwareComponenGuid={5c4c3332-344d-483c-8739-259e934c9cc8}"

REM ------------------- DO NOT MODIFY SECTION ------------------------
:INSTALL
if not exist "%~dp0%DriverPrefix%*" echo [%TIME%] No DCHU driver found. >> %APP_LOG% & goto END
for /f "delims=" %%a in ('dir /ad /b "%~dp0%driverprefix%*"') do (
	echo [%TIME%] Search BASE driver in "%~dp0%%~a\*.inf" >> %APP_LOG%
        dir /a-d /b /s "%~dp0%%~a\*.inf" >nul 2>&1
        if errorlevel 1 echo [%TIME%] No .inf found. >> %APP_LOG% & goto RESULTFAILED
	for /f "delims=" %%i in ('dir /a-d /b /s "%~dp0%%~a\*.inf"') do (
		echo [%TIME%] Check %%~i driver category. >> %APP_LOG%
		call:ChkDrvClassGuid "%%~i" "%ExtensionGuid% %SoftwareComponenGuid%"
		if errorlevel 1 (
			echo [%TIME%] Driver category match, install it. >> %APP_LOG%
			call:DrvInst "%%~i"
			if errorlevel 1 echo [%TIME%] %%~i driver install failed. >> %APP_LOG% & goto RESULTFAILED
			echo [%TIME%] %%~i driver install success. >> %APP_LOG%
		) else (
			echo [%TIME%] Driver category mismatch. >> %APP_LOG%
		)
	)
	echo. >> %APP_LOG%
	echo [%TIME%] Search EXTENSION driver in "%~dp0%%~a\*.inf" >> %APP_LOG%
	for /f "delims=" %%i in ('dir /a-d /b /s "%~dp0%%~a\*.inf"') do (
		echo [%TIME%] Check %%~i driver category. >> %APP_LOG%
		call:ChkDrvClassGuid "%%~i" "%ExtensionGuid%"
		if not errorlevel 1 (
			echo [%TIME%] Driver category match, install it. >> %APP_LOG%
			call:DrvInst "%%~i"
			if errorlevel 1 echo [%TIME%] %%~i driver install failed. >> %APP_LOG% & goto RESULTFAILED
			echo [%TIME%] %%~i driver install success. >> %APP_LOG%
		) else (
			echo [%TIME%] Driver category mismatch. >> %APP_LOG%
		)
	)
	echo. >> %APP_LOG%
	echo [%TIME%] Search COMPONENT driver in "%~dp0%%~a\*.inf" >> %APP_LOG%
	for /f "delims=" %%i in ('dir /a-d /b /s "%~dp0%%~a\*.inf"') do (
		echo [%TIME%] Check %%~i driver category. >> %APP_LOG%
		call:ChkDrvClassGuid "%%~i" "%SoftwareComponenGuid%"
		if not errorlevel 1 (
			echo [%TIME%] Driver category match, install it. >> %APP_LOG%
			call:DrvInst "%%~i"
			if errorlevel 1 echo [%TIME%] %%~i driver install failed. >> %APP_LOG% & goto RESULTFAILED
			echo [%TIME%] %%~i driver install success. >> %APP_LOG%
		) else (
			echo [%TIME%] Driver category mismatch. >> %APP_LOG%
		)
	)
)
REM RESET errorlevel as PREVIOUS section could return 1 for non component drivers.
set errorlevel=0
REM ----------------------------------------------------------------------------------------------------
:lbl_CommonOps
REM ****************************************************
REM *  COMPONENT OWNER TO UPDATE (OPTIONAL COMMANDS)   *
REM *    Please add addition IHV command below.        *
REM ****************************************************

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

Pushd Drivers

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

popd

echo=     
echo **************************************************************
echo ***  Driver Install Finished                                       
echo=

rem if exist %sourcePath% (rd /s/q %sourcePath%)
popd


REM ****************************************************
if NOT "%errorlevel%"=="0" set errcode=%errorlevel%
GOTO END

:DrvInst
echo Pnputil.exe /add-driver "%~1" /install >> %APP_LOG%
Pnputil.exe /add-driver "%~1" /install >> %APP_LOG%
echo Result=%errorlevel% >> %APP_LOG%
if /i [%errorlevel%] == [0] exit /b 0
if /i [%errorlevel%] == [259] exit /b 0
if /i [%errorlevel%] == [3010] exit /b 0
exit /b 1
GOTO:EOF

:ChkDrvClassGuid
if exist c:\system.sav\util\rwini.exe (
    for /f "delims=" %%i in ('c:\system.sav\util\rwini.exe read /file:"%~1" /section:"version" key:"ClassGuid"') do (
        echo ClassGuid=%%~i >> %APP_LOG%.
		for %%x in (%~2) do (if /i [ClassGuid^=%%~i] == [ClassGuid^=%%~x] exit /b 0 )
    )
    exit /b 1
)
for /f "eol=; tokens=1,2 delims== " %%i in ('findstr.exe /i /r /c:"^ClassGuid" "%~1"') do (
    echo ClassGuid=%%~j >> %APP_LOG%
    for %%x in (%~2) do (if /i [%%~i^=%%~j] == [ClassGuid^=%%~x]  exit /b 0)
)
exit /b 1
GOTO:EOF

:RESULTFAILED
ECHO ERRRORLEVEL=%ERRORLEVEL% >> %APP_LOG%
EXIT /B 1
GOTO END

:END
EXIT /B %errcode%

