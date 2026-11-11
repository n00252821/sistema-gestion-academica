"""
Punto de entrada principal para el Sistema de Gestión Académica - Innovatec Education.
"""
from gestion_academica import calcular_promedio, estado_aprobacion, validar_matricula

def main():
    print("=" * 60)
    print("INNOVATEC EDUCATION - SISTEMA DE GESTIÓN ACADÉMICA")
    print("=" * 60)
    
    # Demostración del procesamiento de un estudiante
    estudiante = "Jeremy Joel Lara Arteaga"
    notas = [16.0, 14.5, 18.0, 15.0]
    creditos = 22
    pago_al_dia = True

    print(f"\n[+] Procesando estudiante: {estudiante}")
    
    # 1. Validación de matrícula
    res_matricula = validar_matricula(creditos, pago_al_dia)
    print(f"Estado de Matrícula ({creditos} créditos): {res_matricula['mensaje']}")

    # 2. Cálculo de rendimiento académico
    promedio = calcular_promedio(notas)
    estado = estado_aprobacion(promedio)
    print(f"Notas registradas: {notas}")
    print(f"Promedio Final: {promedio}")
    print(f"Condición Académica: {estado}")
    
    print("\n[OK] Ejecución completada con éxito dentro del contenedor.")
    print("=" * 60)

if __name__ == "__main__":
    main()
