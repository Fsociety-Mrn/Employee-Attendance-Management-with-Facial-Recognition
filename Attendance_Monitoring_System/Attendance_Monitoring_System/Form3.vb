Imports MySqlConnector

Public Class Employee

    Dim oldName As String
    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Me.Close()
    End Sub
    Sub DatatableDat()

        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SELECT * FROM `masterlist`;"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub
    Private Sub Employee_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        DatatableDat()
    End Sub

    Private Sub DataGridView1_CellContentClick(sender As Object, e As DataGridViewCellEventArgs) Handles DataGridView1.CellContentClick
        If e.RowIndex >= 0 Then
            Dim row As DataGridViewRow = DataGridView1.Rows(e.RowIndex)
            oldName = row.Cells(1).Value.ToString
            TextBox3.Text = row.Cells(0).Value.ToString
            TextBox1.Text = row.Cells(1).Value.ToString
            Button1.Enabled = True
        End If
    End Sub
    Public Sub Update()
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            Dim pathsImages As String = "C:\Users\User-PC\Desktop\cognate-I\Pythons\imgs\" +
                oldName + ".png"


            openCon() ''connection 


            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "UPDATE `masterlist` SET `Name` = '" + TextBox1.Text + "' WHERE `ID` = '" + TextBox3.Text + "';"
            mysqlAdapter.SelectCommand = mysqlCommand

            ''dataTable.Clear() ''dataset
            mysqlAdapter.Fill(dataTable)




            My.Computer.FileSystem.RenameFile(pathsImages, TextBox1.Text + ".png")

            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)
            MessageBox.Show("Data has been updated")

            con.Close()

            DatatableDat()
            TextBox1.Text = ""
            TextBox3.Text = ""
            Button1.Enabled = False

        Catch ex As Exception

            MessageBox.Show(ex.ToString)
            con.Close()
            DatatableDat()
        End Try

    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        UpdateEmployee.Show()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        If MessageBox.Show("Are you sure? Do you want to delete this?", "", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation) = DialogResult.Yes Then
            DeleteEmployee.Show()
        End If
    End Sub
    Public Sub Delete()
        Dim pathsImages As String = "C:\Users\User-PC\Desktop\cognate-I\Pythons\imgs\" +
                oldName + ".png"

        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "DELETE FROM `masterlist` WHERE `ID` = '" + TextBox3.Text + "';"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            My.Computer.FileSystem.DeleteFile(pathsImages)

            con.Close()
            MessageBox.Show("Data has successfully deleted")
            DatatableDat()
            TextBox1.Text = ""
            TextBox3.Text = ""
            Button1.Enabled = False

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub
End Class