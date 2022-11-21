Imports MySqlConnector
Public Class attendance
    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
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
    Private Sub attendance_Load(sender As Object, e As EventArgs) Handles MyBase.Load
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
        DatatableDat()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs)
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 
            If Not ComboBox1.Text = "" Then

                If TextBox1.Text = "" Then
                    DatatableDat()
                Else

                    mysqlCommand.Connection = con
                    mysqlCommand.CommandText = "SELECT * FROM `" + ComboBox1.Text + "` WHERE `Name` like '%" & TextBox1.Text & "%';"
                    mysqlAdapter.SelectCommand = mysqlCommand

                    mysqlAdapter.Fill(dataTable)
                    bindingSource.DataSource = dataTable
                    DataGridView1.DataSource = bindingSource
                    mysqlAdapter.Update(dataTable)

                    con.Close()

                End If
            End If

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 
            If Not ComboBox1.Text = "" Then


                mysqlCommand.Connection = con
                    mysqlCommand.CommandText = "SELECT * FROM `" + ComboBox1.Text + "` WHERE `Name` like '%" & TextBox1.Text & "%';"
                    mysqlAdapter.SelectCommand = mysqlCommand

                    mysqlAdapter.Fill(dataTable)
                    bindingSource.DataSource = dataTable
                    DataGridView1.DataSource = bindingSource
                    mysqlAdapter.Update(dataTable)

                    con.Close()

                End If


        Catch ex As Exception

            ''MessageBox.Show(ex.ToString)
            con.Close()
            ''DatatableDat()

        End Try
    End Sub
End Class