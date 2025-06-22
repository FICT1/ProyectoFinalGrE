# dao/OfrendasDao.py
import os
from datetime import datetime
from models.ofrendas import HistoriaOfrendas_dao

ARCHIVO_OFRENDAS = "Historial_Ofrendas.txt"

class Gestion_ofrendasDao:
    def __init__(self):
        self.ofrendas = []
        self.cargar_ofrendas()

    def cargar_ofrendas(self):
        """Carga las ofrendas desde el archivo al iniciar."""
        os.makedirs(os.path.dirname(ARCHIVO_OFRENDAS) or ".", exist_ok=True)
        if os.path.exists(ARCHIVO_OFRENDAS):
            try:
                with open(ARCHIVO_OFRENDAS, "r", encoding='utf-8') as archivo:
                    for linea in archivo:
                        if linea.strip():
                            try:
                                fecha, monto = [x.strip() for x in linea.strip().split(",")]
                                self.ofrendas.append(HistoriaOfrendas_dao(float(monto), fecha))
                            except ValueError as e:
                                print(f"Error al procesar línea '{linea.strip()}': {e}")
                            except Exception as e:
                                print(f"Error inesperado al procesar línea: {e}")
            except IOError as e:
                print(f"Error al leer el archivo de ofrendas: {e}")
                self.ofrendas = []
            except Exception as e:
                print(f"Error inesperado al cargar ofrendas: {e}")
                self.ofrendas = []
        else:
            print(f"Archivo {ARCHIVO_OFRENDAS} no encontrado. Se creará al guardar.")

    def guardar_ofrendas(self):
        """Guarda las ofrendas en el archivo como texto plano, sobrescribiendo el existente."""
        os.makedirs(os.path.dirname(ARCHIVO_OFRENDAS) or ".", exist_ok=True)
        try:
            with open(ARCHIVO_OFRENDAS, "w", encoding='utf-8') as archivo:
                for ofrenda in self.ofrendas:
                    archivo.write(f"{ofrenda.fecha}, {ofrenda.monto:.2f}\n")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
            raise
        except Exception as e:
            print(f"Error inesperado al guardar ofrendas: {e}")
            raise

    def archivar_ofrendas(self, monto):
        """Archiva una nueva ofrenda con la fecha actual."""
        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser mayor que cero.")
            fecha = datetime.now().strftime("%Y-%m-%d")
            ofrenda = HistoriaOfrendas_dao(monto, fecha)
            if not isinstance(ofrenda, HistoriaOfrendas_dao):
                raise ValueError("No se pudo crear una instancia válida de HistoriaOfrendas_dao")

            os.makedirs(os.path.dirname(ARCHIVO_OFRENDAS) or ".", exist_ok=True)
            if not os.path.exists(ARCHIVO_OFRENDAS):
                with open(ARCHIVO_OFRENDAS, "w") as archivo:
                    pass  # Crear archivo vacío

            # Sincronizar antes de escribir
            self.ofrendas.append(ofrenda)
            self.guardar_ofrendas()
            print(f"Ofrenda de C${monto:.2f} archivada el {fecha} en {ARCHIVO_OFRENDAS}")
        except ValueError as e:
            print(f"Error: {e}")
            raise
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
            raise
        except Exception as e:
            print(f"Error inesperado al archivar ofrenda: {e}")
            raise

    def mostrar_ofrendas(self):
        """Muestra una lista del historial de ofrendas ingresadas con su fecha y monto."""
        if not self.ofrendas:
            print("No hay ofrendas archivadas.")
            return
        print("\n=== Lista de Ofrendas Registradas ===")
        print(f"{'Fecha':<12} {'Monto':>10}")
        print("-" * 24)
        for ofrenda in self.ofrendas:
            try:
                if not isinstance(ofrenda, HistoriaOfrendas_dao):
                    print(f"Error: Instancia inválida en la lista de ofrendas: {ofrenda}")
                    continue
                fecha = str(ofrenda.fecha)[:12]
                monto = float(ofrenda.monto)
                print(f"{fecha:<12} C${monto:>8.2f}")
            except (AttributeError, ValueError) as e:
                print(f"Error al procesar una ofrenda: {e}")
        print("=" * 24)

    def eliminar_ofrenda(self, monto):
        """Elimina una ofrenda por monto con opción de selección por fecha."""
        if not os.path.exists(ARCHIVO_OFRENDAS):
            print("No hay ofrendas archivadas.")
            return False

        try:
            monto = float(monto)
            if monto <= 0:
                raise ValueError("El monto debe ser mayor que cero.")

            with open(ARCHIVO_OFRENDAS, "r", encoding='utf-8') as archivo:
                lineas = archivo.readlines()

            coincidencias = [(fecha, m, linea) for linea in lineas if linea.strip()
                           for fecha, m in [linea.strip().split(", ")]
                           if abs(float(m) - monto) < 0.01]

            if not coincidencias:
                print(f"No se encontró una ofrenda de C${monto:.2f}.")
                return False

            print(f"Se encontraron {len(coincidencias)} ofrenda(s) de C${monto:.2f}:")
            for i, (fecha, _, _) in enumerate(coincidencias, 1):
                print(f"{i}. Fecha: {fecha}, Monto: C${monto:.2f}")

            opcion = input("Seleccione número, 'todas' o 'cancelar': ").strip().lower()
            if opcion == "cancelar":
                print("Operación cancelada.")
                return False

            nuevas_lineas = lineas
            if opcion == "todas":
                nuevas_lineas = [linea for linea in lineas if linea not in [c[2] for c in coincidencias]]
                self.ofrendas = [o for o in self.ofrendas if abs(float(o.monto) - monto) >= 0.01]
                print(f"Todas las ofrendas de C${monto:.2f} eliminadas.")
            else:
                try:
                    indice = int(opcion) - 1
                    if 0 <= indice < len(coincidencias):
                        nuevas_lineas = [linea for linea in lineas if linea != coincidencias[indice][2]]
                        self.ofrendas = [o for o in self.ofrendas if not (abs(float(o.monto) - monto) < 0.01 and o.fecha == coincidencias[indice][0])]
                        print(f"Ofrenda de C${monto:.2f} del {coincidencias[indice][0]} eliminada.")
                    else:
                        print("Selección inválida.")
                        return False
                except ValueError:
                    print("Entrada inválida.")
                    return False

            with open(ARCHIVO_OFRENDAS, "w", encoding='utf-8') as archivo:
                archivo.writelines(nuevas_lineas)
            return True

        except ValueError as e:
            print(f"Error: {e}")
            return False
        except IOError as e:
            print(f"Error al acceder al archivo: {e}")
            return False
        except Exception as e:
            print(f"Error inesperado: {e}")
            return False

    def calcular_total_ofrendas(self):
        """Calcula y muestra el total de todas las ofrendas."""
        if not self.ofrendas:
            print("No hay ofrendas archivadas para calcular el total.")
            return 0.0
        try:
            total = sum(float(ofrenda.monto) for ofrenda in self.ofrendas)
            print(f"\n=== Total de Ofrendas ===")
            print(f"Total: C${total:.2f}")
            print("=" * 24)
            return total
        except (AttributeError, ValueError) as e:
            print(f"Error al calcular total: {e}")
            return 0.0