"""Genera la memoria académica con resultados comprobados al 15-11-2026."""

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/memoria-tecnica-pulseops.pdf"
FONT = Path("C:/Windows/Fonts/arial.ttf")
FONT_BOLD = Path("C:/Windows/Fonts/arialbd.ttf")
pdfmetrics.registerFont(TTFont("Arial", str(FONT)))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(FONT_BOLD)))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontName="Arial-Bold", fontSize=22, leading=27,
                          textColor=colors.HexColor("#16324f"), alignment=TA_CENTER, spaceAfter=20))
styles.add(ParagraphStyle(name="SectionPulse", fontName="Arial-Bold", fontSize=12, leading=16,
                          textColor=colors.HexColor("#16324f"), spaceBefore=12, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyPulse", fontName="Arial", fontSize=9, leading=13, spaceAfter=7))
styles.add(ParagraphStyle(name="SmallPulse", fontName="Arial", fontSize=8, leading=11, spaceAfter=5))
styles.add(ParagraphStyle(name="TablePulse", fontName="Arial", fontSize=8, leading=11))


def para(text, style="BodyPulse"):
    return Paragraph(text, styles[style])


def link(label, url):
    return f'<link href="{escape(url)}" color="#0866a5">{escape(label)}</link>'


def table(rows, widths):
    data = [[para(str(cell), "TablePulse") for cell in row] for row in rows]
    result = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e8f0f7")),
        ("GRID", (0, 0), (-1, -1), .35, colors.HexColor("#b6c4d0")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Arial", 8)
    canvas.setFillColor(colors.HexColor("#52677a"))
    canvas.drawString(1.8 * cm, 1.2 * cm, "PulseOps | Práctica final CI/CD")
    canvas.drawRightString(A4[0] - 1.8 * cm, 1.2 * cm, str(doc.page))
    canvas.restoreState()


story = [Spacer(1, 1.5 * cm), para("PulseOps<br/>Memoria técnica CI/CD", "CoverTitle"),
         para("Práctica final de Despliegue de Software. Estado comprobado el 15 de noviembre de 2026 (Bogotá)."),
         para("Objetivo y arquitectura", "SectionPulse"),
         para("GitHub <b>main</b> → Azure DevOps CI → artefacto <b>webapp-drop</b> → Azure DevOps CD → Azure App Service. Node.js 22, TypeScript, Express, HTML y CSS. La página muestra estado, versión y SHA; <b>/api/health</b> ofrece los mismos datos en JSON."),
         para("Equipo y responsabilidades", "SectionPulse"),
         table([["Área", "Responsable"], ["Frontend", "Carla Juliana Giraldo Camacho · carlagiraldo09"],
                ["CI", "Samuel · samuelcuello05 (nombre completo pendiente)"],
                ["CD y Azure", "Carolina Arango Escobar · caro-a21"],
                ["QA", "Daniel Felipe Marin Marin · Dazzlm"],
                ["Integración", "Tomas Gonzalez Zapata · tomasgonzalez0"]], [3.3 * cm, 13.6 * cm]),
         Spacer(1, .35 * cm),
         para("El equipo confirmó trabajo conjunto en un mismo PC. Los commits funcionales tienen autor y committer del responsable asignado; GitHub registra por separado la cuenta de push o merge. La aprobación de una revisión solo se atribuye si aparece en el historial del PR."),
         para("Repositorio y ejecución local", "SectionPulse"),
         para(link("Repositorio GitHub", "https://github.com/tomasgonzalez0/pulseops-azure-delivery") + ". El docente oalarconpe tiene una invitación de lectura pendiente. <b>npm ci</b>, <b>npm test</b> y <b>npm start</b> permiten reproducir la aplicación local; la prueba automatizada del endpoint pasó 1/1."),
         PageBreak(),
         para("CI: configuración y ejecuciones", "SectionPulse"),
         para("La pipeline " + link("PulseOps CI-CD", "https://dev.azure.com/carlagiraldo327724/PulseOps/_build?definitionId=1") + " (ID 1) usa el repositorio GitHub, trigger para <b>main</b> y agente hospedado <b>ubuntu-22.04</b>. CI instala desde package-lock.json, compila TypeScript, ejecuta pruebas, crea un ZIP de producción y publica <b>webapp-drop</b>."),
         table([["Run", "SHA de main", "Resultado comprobado"],
                [link("#11", "https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=11&view=results"), "515d2995…", "CI, pruebas y artefacto exitosos; CD falló por cuota del plan F1 compartido."],
                [link("#13", "https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=13&view=results"), "cb39e800…", "Automática: CI y CD exitosas; versión 1 y health HTTP 200."],
                [link("#15", "https://dev.azure.com/carlagiraldo327724/PulseOps/_build/results?buildId=15&view=results"), "530c3e7a…", "Automática: CI y CD exitosas; versión 2 visible y health HTTP 200."]], [2 * cm, 3 * cm, 11.9 * cm]),
         para("Los primeros runs no encontraron un agente en Azure Pipelines. Se activó un trabajo Microsoft-hosted gratuito (1.800 min/mes, 0 trabajos comprados) y se fijó ubuntu-22.04. Los runs #13 y #15 ejecutaron ambas etapas con agente hospedado; no se instaló uno en el PC."),
         para("CD, Azure y seguridad", "SectionPulse"),
         para("CD depende de CI exitosa y descarga <b>webapp-drop/pulseops.zip</b> de la misma ejecución, sin recompilar. AzureWebApp@1 usa la conexión <b>PulseOps Azure WIF</b> con federación sin secreto. Su principal tiene rol Contributor limitado al App Service <b>pulseops-delivery-itm-2026</b>. No se almacenaron tokens en GitHub."),
         para("La aplicación Linux Node 22 está en el plan gratuito LinuxFree F1 <b>asp-pulseops-f1</b>, grupo <b>rg-pulseops-delivery</b>, Brazil South. URL: " + link("pulseops-delivery-itm-2026.azurewebsites.net", "https://pulseops-delivery-itm-2026.azurewebsites.net") + ". No se compró capacidad adicional. El plan F1 anterior, compartido con inventario, produjo QuotaExceeded y HTTP 403 para ambas. Tras verificar la versión 2, se eliminó solo el App Service antiguo de PulseOps; inventario y su plan permanecen."),
         PageBreak(),
         para("Trazabilidad del cambio visible", "SectionPulse"),
         para("La versión 1 quedó en el merge del PR #14, SHA <b>cb39e80043a4fc08b6aac298e8ee8bc6bb001473</b>. El run automático #13 publicó el artefacto, lo desplegó y la API devolvió ese SHA con versión 1."),
         para("El PR " + link("#15", "https://github.com/tomasgonzalez0/pulseops-azure-delivery/pull/15") + " cambió la página y la API a versión 2. Su merge en main produjo el SHA <b>530c3e7a0025fbeac3f9de70a2b2e5de79605916</b>. El run automático #15 terminó con build, pruebas, publicación, descarga, despliegue y health check exitosos. La consulta externa devolvió HTTP 200, versión 2 y el mismo SHA; la página mostró «PulseOps — Version 2»."),
         para("Respuesta pública comprobada", "SectionPulse"),
         para('<font name="Arial">{"status":"ok","app":"PulseOps","version":"2",<br/>"build":"530c3e7a0025fbeac3f9de70a2b2e5de79605916"}</font>', "SmallPulse"),
         para(link("Abrir /api/health", "https://pulseops-delivery-itm-2026.azurewebsites.net/api/health")),
         para("Evidencias visuales y audiovisuales pendientes", "SectionPulse"),
         para("[CAPTURAS REALES PENDIENTES] Añadir imágenes del run #15: causa individualCI y SHA; compilación y prueba; artefacto webapp-drop; descarga en CD; AzureWebApp y health check; página pública versión 2. Las carpetas evidencias/ci y evidencias/cd están preparadas. No se fabricaron imágenes."),
         para("[VIDEOS PENDIENTES] Grabar dos videos narrados, uno de CI y otro de CD, con participación de los cinco integrantes. Añadir enlaces a README y a esta memoria, y entregar los materiales en Teams. La invitación del docente sigue pendiente de aceptación."),
         para("Conclusión y alcance", "SectionPulse"),
         para("El flujo GitHub → CI → webapp-drop → CD → Azure App Service está comprobado en dos ejecuciones automáticas. El cambio visible conserva el mismo SHA desde el merge hasta /api/health. La evidencia técnica enlazada permite auditarlo; capturas, videos y entrega institucional siguen siendo tareas humanas."),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=1.8*cm,
                        leftMargin=1.8*cm, topMargin=1.8*cm, bottomMargin=1.9*cm,
                        title="PulseOps - Memoria técnica CI/CD", author="Equipo PulseOps")
doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
print(OUTPUT)
