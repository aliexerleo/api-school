import psycopg2 
from psycopg2 import Error
from connection import create_connection


def all_courses():
	conn = create_connection()
	sql = """ SELECT 
				  C_C.nombre 
			  FROM colegio1_cursos C_C
			  ORDER BY id """

	try:
		cur = conn.cursor()
		cur.execute(sql)
		query = cur.fetchall()
		return query
	except Error as e:
		print('Error at all_courses(): {str(e)}')
		return False
	finally:
		if conn:
			cur.close()
			conn.close()

def asignatures_sixth():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 2"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_sixth(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()

def asignatures_seventh():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 3"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_seventh(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()


def asignatures_eighth():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 4"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_eighth(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()


def asignatures_ninth():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 5"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_ninth(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()

def asignatures_tenth():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 6"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_tenth(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()

def asignatures_eleventh():
	conn = create_connection()
	sql = """SELECT 
				    A_S.nombre
			  FROM colegio1_asignaturas A_S
			  WHERE curso_id = 7"""
	try:
	    cur = conn.cursor()
	    cur.execute(sql)
	    query = cur.fetchall()
	    return query
	except Error as e:
		print('Error at asignatures_eleventh(): {str(e)}')
	finally:
		if conn:
			cur.close()
			conn.close()


def courses(id):
	conn = create_connection()
	sql = """SELECT  
					C_S.nombre, 
					A_G.nombre 
			 FROM colegio1_cursos C_S 
			 	INNER JOIN colegio1_asignaturas A_G ON C_S.id = A_G.curso_id 
			 WHERE C_S.id = {id}"""
			 #WHERE C_S.id = {id} """.format(id=id)

	try:
		cur = conn.cursor()
		cur.execute(sql)
		query = cur.fetchall()
		return query
	except Error as e:
		print('Error at select_data(): {str(e)}')
		return False
	finally:
		if conn:
			cur.close()
			conn.close()

