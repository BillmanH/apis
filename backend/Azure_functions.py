def getCursor():
        conn = pymssql.connect(server=DBServer, user=DBAccessUser, password=DBAccessPassword, database=DBDatabase)  
        cursor = conn.cursor()  
        return cursor, conn

def getWeeklyAverages():
        cursor, conn = getCursor()
        cursor.execute("""
                Select myCol
                , AVG([Amount]) as [Average]
                from (
                        select
                        DATENAME(WEEKDAY,[Date of pull]-1) as myCol
                        ,[Amount]
                        from 
                        dbo.Transaction2
                        where [Date of pull] > GETDATE()-130
                ) A
                group by myCol
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

def getYesterdaysTransactions():
        cursor, conn = getCursor()
        cursor.execute("""
                Select *  
                from 
                dbo.Transaction2
                where [Date of pull] >  GETDATE()-2
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows
