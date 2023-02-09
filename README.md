# baufestest


## Allure Docs (Para generacion de Reporte)
- https://docs.qameta.io/allure/
- Instalacion de libreria Allure en los diferentes SO:
- Mac OS
> brew install allure
- Windows
> scoop install allure
- Linux
> sudo apt-get install allure

## Instalacion de requerimientos

- Primero que nada tener instalado Python en el Ordenador

- Ejecutar en la ruta del proyecto el siguiente comando:
> pip install -r .\requirements

## Comando de ejecucion

- Para una ejecucion simple basta con ubicarse en la ruta ./baufestest/src y escribir el siguiente comando:
> behave
- Para una ejecucion con generacion de reporte el siguiente comando misma ruta ./baufestest/src:
> behave --format allure_behave.formatter:AllureFormatter -o allure-results
- luego generar en base a los resultados de con este comando:
> allure generate allure-results --clean
- y para visualizarlo:
> allure open

