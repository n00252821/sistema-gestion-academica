"""
Sistema de Gestión Integral de Servicios Académicos - Innovatec Education
Módulo de lógica de negocio para estudiantes, matrículas y cálculo de calificaciones.
"""

def calcular_promedio(notas: list[float]) -> float:
    """Calcula el promedio ponderado o simple de una lista de notas (0 a 20)."""
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    for n in notas:
        if n < 0 or n > 20:
            raise ValueError(f"Nota inválida: {n}. Debe estar entre 0 y 20.")
    return round(sum(notas) / len(notas), 2)


def estado_aprobacion(promedio: float) -> str:
    """Determina si el estudiante está aprobado o desaprobado (Nota mínima 13 en UPN)."""
    if promedio < 0 or promedio > 20:
        raise ValueError("Promedio fuera de rango (0 - 20).")
    return "APROBADO" if promedio >= 12.5 else "DESAPROBADO"


def validar_matricula(creditos: int, pago_al_dia: bool) -> dict:
    """Valida si un estudiante puede matricularse según créditos y estado de pagos."""
    if creditos <= 0 or creditos > 26:
        return {"valido": False, "mensaje": "Créditos fuera del rango permitido (1 a 26 créditos)."}
    if not pago_al_dia:
        return {"valido": False, "mensaje": "Matrícula rechazada por deuda pendiente."}
    return {"valido": True, "mensaje": "Matrícula procesada correctamente."}
