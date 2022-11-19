Imports MySqlConnector

Module Database
    Public con As New MySqlConnection
    Public mysqlCommand As New MySqlCommand
    Public mysqlAdapter As New MySqlDataAdapter
    Public data As New DataSet


    Sub openCon()
        Dim localhost As String = "localhost"
        Dim username As String = "root"
        Dim password As String = ""
        Dim database As String = "cognate1"
        con.ConnectionString = "server=" + localhost +
            ";username=" + username +
            ";password=" + password +
            ";database=" + database
        con.Open()
    End Sub
End Module
