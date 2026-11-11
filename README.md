# Sistema de Gestión Académica - Innovatec Education

Proyecto desarrollado para la evaluación **T3 de Calidad y Pruebas de Software (UPN)**.

## Integrante
* **Estudiante:** Jeremy Joel Lara Arteaga
* **Código / GitHub:** [n00252821](https://github.com/n00252821)
* **NRC:** 26107

---

## Descripción del Proyecto
Este sistema implementa la lógica central para la gestión académica de Innovatec Education:
1. Validación de matrícula basada en límites de créditos y pagos al día.
2. Cálculo de promedios académicos y determinación del estado de aprobación.
3. Suite de pruebas unitarias automatizadas con `unittest`.
4. Integración Continua (CI) mediante **GitHub Actions**.
5. Contenerización y ejecución portátil con **Docker**.

---

## Ejecución Local de Pruebas Unitarias

```bash
python test_gestion_academica.py -v
```

---

## Ejecución con Docker

### 1. Construir la imagen
```bash
docker build -t sistema-academico .
```

### 2. Verificar la imagen creada
```bash
docker images
```

### 3. Ejecutar el contenedor
```bash
docker run --rm sistema-academico
```
