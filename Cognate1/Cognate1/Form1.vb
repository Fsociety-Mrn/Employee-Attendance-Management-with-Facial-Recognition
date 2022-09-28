Imports MySql.Data.MySqlClient
Public Class Form1
    Private Sub Button1_Click(sender As Object, e As EventArgs)
        MessageBox.Show("Hello Friend")
    End Sub

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SHOW TABLES;"
            mysqlAdapter.SelectCommand = mysqlCommand

            data.Clear() ''dataset
            mysqlAdapter.Fill(data)

            Dim myread As MySqlDataReader = mysqlCommand.ExecuteReader


            While myread.Read
                ComboBox1.Items.Add(myread(0))
            End While

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
        End Try

    End Sub



    Private Sub ComboBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles ComboBox1.SelectedIndexChanged

        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SELECT * FROM `" + ComboBox1.Text + "`;"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
        End Try
    End Sub
End Class
