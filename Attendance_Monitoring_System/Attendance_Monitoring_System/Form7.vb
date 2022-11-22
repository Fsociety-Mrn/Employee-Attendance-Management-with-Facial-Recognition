﻿Imports MySqlConnector
Public Class Report
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Me.Close()
    End Sub
    Sub DatatableDat()

        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 
            If Not ComboBox1.Text = "" Then


                mysqlCommand.Connection = con
                mysqlCommand.CommandText = "SELECT * FROM `" + ComboBox1.Text + "`;"
                mysqlAdapter.SelectCommand = mysqlCommand

                mysqlAdapter.Fill(dataTable)
                bindingSource.DataSource = dataTable
                DataGridView1.DataSource = bindingSource
                mysqlAdapter.Update(dataTable)

                con.Close()
            End If

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub
    Private Sub Report_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SHOW TABLES;"
            mysqlAdapter.SelectCommand = mysqlCommand

            data.Clear() ''dataset
            mysqlAdapter.Fill(data)

            Dim myread As MySqlDataReader = mysqlCommand.ExecuteReader


            While myread.Read
                If Not myread(0) = "admin" And Not myread(0) = "masterlist" Then
                    ComboBox1.Items.Add(myread(0))
                End If

            End While

            con.Close()

            ComboBox1.SelectedIndex = 0

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub

    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged
        DatatableDat()
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        PrintDocument1.Print()
    End Sub

    Private Sub PrintDocument1_PrintPage(sender As Object, e As Printing.PrintPageEventArgs) Handles PrintDocument1.PrintPage
        Dim imgbmp As New Bitmap(Me.DataGridView1.Width, Me.DataGridView1.Height)
        DataGridView1.DrawToBitmap(imgbmp, New Rectangle(0, 0, Me.DataGridView1.Width, Me.DataGridView1.Height))


        e.Graphics.DrawString("Attendance Monitoring System",
                              New Font("Century Gothic", 15, FontStyle.Bold),
                              Brushes.Black,
                               270, 30)

        e.Graphics.DrawString(ComboBox1.Text,
                              New Font("Century Gothic", 15, FontStyle.Bold),
                              Brushes.Black,
                               270, 60)
        e.Graphics.DrawImage(imgbmp, 200, 100)

    End Sub
End Class