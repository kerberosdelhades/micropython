@echo off
set WORKING_DIRECTORY=H:\Python
set CONFIG_FILE=%UserProfile%\.thonny\configuration.ini
echo [view] > %CONFIG_FILE%
echo shellview.visible = True >> %CONFIG_FILE%
echo globalsview.visible = True >> %CONFIG_FILE%
echo objectinspector.visible = True >> %CONFIG_FILE%
echo show_line_numbers = True >> %CONFIG_FILE%
echo recommended_line_length = 80 >> %CONFIG_FILE%
echo. >> %CONFIG_FILE%
echo [run] >> %CONFIG_FILE%
echo working_directory = %WORKING_DIRECTORY% >> %CONFIG_FILE%
mkdir %WORKING_DIRECTORY%
echo "Thonny se ha configurado correctamente."
pause
