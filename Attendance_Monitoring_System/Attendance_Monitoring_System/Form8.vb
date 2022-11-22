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
            Button4.Enabled = True

        Catch ex As Exception
            MessageBox.Show("Data has not yet been created.")
            con.Close()
            Button4.Enabled = False
        End Try
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        ''PrintPreviewDialog1.ShowDialog()
        PrintDocument1.Print()
    End Sub

    Private Sub PrintDocument1_PrintPage(sender As Object, e As Printing.PrintPageEventArgs) Handles PrintDocument1.PrintPage
        Dim imgbmp As New Bitmap(Me.DataGridView1.Width, Me.DataGridView1.Height)
        DataGridView1.DrawToBitmap(imgbmp, New Rectangle(0, 0, Me.DataGridView1.Width, Me.DataGridView1.Height))


        e.Graphics.DrawString("Attendance Monitoring System",
                              New Font("Century Gothic", 15, FontStyle.Bold),
                              Brushes.Black,
                               270, 30)

        e.Graphics.DrawString(DateTimePicker1.Text,
                              New Font("Century Gothic", 15, FontStyle.Bold),
                              Brushes.Black,
                               270, 60)
        e.Graphics.DrawImage(imgbmp, 200, 100)

    End Sub
End Class