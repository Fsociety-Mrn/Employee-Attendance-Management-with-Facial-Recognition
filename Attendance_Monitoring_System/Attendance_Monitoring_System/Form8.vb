Imports MySqlConnector
Public Class Form8
    Private Sub Form8_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        DateTimePicker1.Format = DateTimePickerFormat.Custom
        DateTimePicker1.CustomFormat = "yyyy-MM-dd"


        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SELECT * FROM `" + DateTimePicker1.Text + "`;"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            con.Close()

        Catch ex As Exception
            MessageBox.Show("Data has not yet been created.")
            con.Close()
        End Try
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click

    End Sub
End Class