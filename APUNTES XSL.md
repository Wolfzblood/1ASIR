- XSLT (Transformation)
- XSL-FO (XSL Formatting Objects)
- XPath (Consultas)

# XSLT

Con XSLT se puede transformar un documento expresado en el formato XML en un documento equivalente expresado en otro formato, normalmente HTML.

## Estructura

Los componentes que forman parte de una transformacion son:
	- Documento XML
	- Fichero de transformacion
	-  Un procesador (editor o página web)

El documento XML debe tener una referencia al documento XSL.
```xml
<?xml version=”1.0” encoding=”UTF-8”?>
<?xml-stylesheet type="text/xsl" href="ejemplo1.xsl">
```

La estructura del documento XSL debe incluir la declaración del espacio de nombres de XSL y el elemento que indica que se debe aplicar la transformación a todo el documento XML o a partes del mismo.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">
...
</xsl:template>
</xsl:stylesheet>
```

Una hoja de transformaciones debe ir compuesta por lo siguiente:

- Declaracion del documento XML.
	```xml
	<?xml versión=”1.0?”>
	```
- Elemento raíz.
	```xml
	<xsl:stylesheet versión=”1.0”
	xmlns= “http://www.w3.org/1999/XSL/Transform”
	…
	/xsl:stylesheet>
	```
- Espacio de nombres.

En el documento XSL se alterna texto libre (HTML) con elementos XSL.
- Los textos libres se mostrarán sin ninguna modificación.
- Los elementos XSL son los que aportan las reglas de transformación.

**EJEMPLO**

Documento XML.
```XML
<?xml version="1.0" encoding='ISO-8859-1'?>
<?xml-stylesheet href="tienda-html.xsl" type="text/xsl"?>
<tienda>
	<nombre> La tiendecilla </nombre>
	<telefono> 983 25 12 23 </telefono>
</tienda>
```

Reglas de transformacion XSLT (.xsl)
```XML
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match='/'>
	<html>
		<head><title>Generado con tienda-html.xsl</title></head>
		<body>
			<h1> <xsl:value-of select="tienda/nombre"/> </h1>
			<h2> <xsl:value-of select="tienda/telefono"/> </h2>
		</body>
	</html>
</xsl:template>
</xsl:stylesheet>
```

El elemento siguiente indica que nos encontramos ante una transformación.
```XML
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

```

El elemento <xsl:template> se usa para crear una plantilla. En este caso como se pone "/" pues afecta a todo el documento.
```XML
<xsl:template match='/'>
```

Los elementos <xsl:value-of> indican que deben ser sustituidos por el valor del elemento obtenido.
```XML
<h1> <xsl:value-of select="tienda/nombre"/> </h1>
<h2> <xsl:value-of select="tienda/telefono"/> </h2>
```

El resto es código HTML. 

**Se puede generar cualquier salida en formato texto a partir de un documento XML.**

### Plantillas.

Las plantillas son pratones para la transformación.

Hay dos partes, está la platilla y patrón de busqueda.

```XML
<xsl:template match='/'>
```


**EJEMPLO**

```XML
<xsl:template match='/’>
	<html>
	<head>
		<title>Título ejemplo</title></head>
	<body>
		<h1> <xsl:apply-templates /> </h1>
	</body>
	</html>
</xsl:template>
```

El elemento <xsl:apply-templates>, se utiliza para llamar a otras y si no hay otras se usa la de por defecto.

```XML
<xsl:apply-templates select=”expresión XPath”>
```

Por ejemplo, aquí se usa el apply templates para la segunda template.
```XML
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match='/'>
	<html>
		<head>
			<title>Ejemplo1 </title></head>
		<body>
			<xsl:apply-templates />
		</body>
	</html>
</xsl:template>
<xsl:template match="nombre">
<p> He encontrado una persona del grupo</p>
</xsl:template>
</xsl:stylesheet>
```

El elemento <xsl:value-of>, se usa para obtener el contenido de los nodos.
```XML
<xsl:value-of select=”expresión XPath”>
```

Si yo pongo esto:
```XML
<xsl:template match="nombre">
<p> <xsl:value-of select="." /> </p>
</xsl:template>
</xsl:stylesheet>
```

Se vería esto:
![[Pasted image 20230527135706.png]]

El elemento <xsl:text>, inserta texto.
```XML
</xsl:template>
<xsl:template match="nombre">
<p> <xsl:text > Un nombre: </xsl:text> <xsl:value-of select="." /> </p>
</xsl:template>
```
![[Pasted image 20230527135854.png]]

El elemento <xsl:element> permite incluir elementos en base a texto libre.
```XML
 <?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match='/'>
<html>
	<head><title>Ejemplo4 </title></head>
	<body>Los nombres en una lista:
		<xsl:element name="ul" > <xsl:apply-templates /> </xsl:element>
	</body>
</html>
</xsl:template>
<xsl:template match="nombre">
	<xsl:element name="li"> <xsl:text > Un nombre </xsl:text>
			<xsl:value-of select="." />
	</xsl:element>
</xsl:template>
</xsl:stylesheet>
```
![[Pasted image 20230527140311.png]]

El documento hace que se cree una lista.




# XPATH

Los patrones pueden ser muy complejos, se caracteriza por ser declarativo o ser contextual.

Estos son los operadores mas usados.
![[Pasted image 20230527132118.png]]

