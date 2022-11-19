Imports MySqlConnector

Public Class login
    Private Sub Button2_Click(sender As Object, e As EventArgs)
        Me.Close()

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim username As String
        Dim password As String
        username = txtUser.Text
        password = txtPass.Text

        Dim query As String = "SELECT `ID` FROM `admin` WHERE username='" +
            username + "' AND password='" + password + "';"

        Try
            openCon() ''open connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = query
            mysqlAdapter.SelectCommand = mysqlCommand

            data.Clear() ''dataset
            mysqlAdapter.Fill(data)

            Dim myread As MySqlDataReader = mysqlCommand.ExecuteReader

            If myread.Read Then
                MessageBox.Show("Login Success", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
                dashboard.Show()
                Me.Hide()

            Else
                MessageBox.Show("Please double-check your username and password.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Error)
            End If

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
        End Try

    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Application.Exit()
    End Sub
End Class
