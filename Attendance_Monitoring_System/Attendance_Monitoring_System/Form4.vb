Imports MySqlConnector
Public Class Monitoring
    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Me.Close()
    End Sub
    Sub DatatableDat()

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
    Private Sub Monitoring_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        DateTimePicker1.Hide()
        Label3.Text = DateTimePicker1.Text

        DateTimePicker1.Format = DateTimePickerFormat.Custom
        DateTimePicker1.CustomFormat = "yyyy-MM-dd"
        DatatableDat()

        ''add combox name
        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "SELECT `Name` FROM `" + DateTimePicker1.Text + "`;"
            mysqlAdapter.SelectCommand = mysqlCommand

            data.Clear() ''dataset
            mysqlAdapter.Fill(data)

            Dim myread As MySqlDataReader = mysqlCommand.ExecuteReader


            While myread.Read
                ComboBox1.Items.Add(myread(0))
            End While

            ComboBox1.SelectedIndex = 0

            con.Close()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try

    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        If MessageBox.Show("Are you sure? Do you want to delete this?", "", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation) = DialogResult.Yes Then
            onTimeTodayDeleteForm.Show()
        End If

    End Sub
    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        If ComboBox1.Text = "" Then
            DatatableDat()
        Else
            Dim bindingSource As New BindingSource
            Dim dataTable As New DataTable

            Try
                openCon() ''connection 

                mysqlCommand.Connection = con
                mysqlCommand.CommandText = "SELECT * FROM `" + DateTimePicker1.Text + "` WHERE `Name` = '" + ComboBox1.Text + "';"
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
        End If
    End Sub

    Private Sub Button4_Click(sender As Object, e As EventArgs) Handles Button4.Click
        DatatableDat()
    End Sub

    Sub Delete()
        Dim bindingSource As New BindingSource
        Dim dataTable As New DataTable

        Try
            openCon() ''connection 

            mysqlCommand.Connection = con
            mysqlCommand.CommandText = "DELETE FROM `" + DateTimePicker1.Text +
                "` WHERE `Name` = '" + DataGridView1.CurrentRow.Cells(0).Value.ToString + "';"
            mysqlAdapter.SelectCommand = mysqlCommand

            mysqlAdapter.Fill(dataTable)
            bindingSource.DataSource = dataTable
            DataGridView1.DataSource = bindingSource
            mysqlAdapter.Update(dataTable)

            con.Close()

            DatatableDat()

        Catch ex As Exception
            MessageBox.Show(ex.ToString)
            con.Close()
        End Try
    End Sub
End Class