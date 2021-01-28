
 DECLARE @tableName VARCHAR(200)  
SET @tableName=''  
WHILE EXISTS  
 (  
 --Find all child tables AND those which have no relations  
             SELECT T.table_name FROM INFORMATION_SCHEMA.TABLES T  
             LEFT OUTER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC  
             ON T.table_name=TC.table_name  
             WHERE (TC.constraint_Type ='Foreign Key'or TC.constraint_Type IS NULL) AND  
             T.table_name NOT IN ('dtproperties','sysconstraints','syssegments')AND  
             Table_type='BASE TABLE' AND T.table_name > @TableName  
 )  
 BEGIN  
             SELECT @tableName=min(T.table_name) FROM INFORMATION_SCHEMA.TABLES T  
             LEFT OUTER JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS TC  
             ON T.table_name=TC.table_name  
             WHERE (TC.constraint_Type ='Foreign Key'or TC.constraint_Type IS NULL) AND  
             T.table_name NOT IN ('dtproperties','sysconstraints','syssegments') AND  
             Table_type='BASE TABLE' AND T.table_name > @TableName  
             --Truncate the table  
             EXEC('DELETE FROM '+@tablename)  
     PRINT 'DELETE FROM '+@tablename  
 END 