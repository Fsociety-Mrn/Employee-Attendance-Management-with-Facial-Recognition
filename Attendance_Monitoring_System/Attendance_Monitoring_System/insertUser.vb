﻿Imports MySqlConnector
Public Class insertUser
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim query As String = "SELECT `ID` FROM `admin` WHERE password='" + txtPass.Text + "';"

        Try
            openCon() ''open connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = query
            mysqlAdapter.SelectCommand = mysqlCommand

            data.Clear() ''dataset
            mysqlAdapter.Fill(data)

            Dim myread As MySqlDataReader = mysqlCommand.ExecuteReader

            If myread.Read Then
                MessageBox.Show("Password completed", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
                con.Close()
                txtPass.Text = ""
                user.Insert()
                Me.Hide()
                user.Enabled = True
                user.Show()

            Else
                MessageBox.Show("Please double-check your password.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Error)
            End If

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
        End Try
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Me.Hide()
        user.Enabled = True
        user.Show()
    End Sub
End Class