from nose.tools import assert_equal

from jenkinsdashboard.ui.ui import Cell, Row


def test_cell_left_padding():
    cell = Cell("TEST", True)
    rendered = cell.left_padding("TEST", 10)
    assert_equal(rendered, "      TEST")


def test_cell_right_padding():
    cell = Cell("TEST", True)
    rendered = cell.right_padding("TEST", 10)
    assert_equal(rendered, "TEST      ")


def test_cell_render_value_smaller_than_width_right_aligned():
    cell = Cell("TEST", True)
    cell.render(10)
    assert_equal(cell.rendered_value, "      TEST")


def test_cell_render_value_smaller_than_width_left_aligned():
    cell = Cell("TEST", False)
    cell.render(10)
    assert_equal(cell.rendered_value, "TEST      ")


def test_cell_render_value_larger_than_width():
    cell = Cell("TESTTESTTEST", False)
    cell.render(10)
    assert_equal(cell.rendered_value, "TESTTESTTE")


def test_row_render_two_columns():
    cell1 = Cell("TEST1", False)
    cell2 = Cell("TEST2", True)
    row = Row([cell1, cell2], 50)
    row.render()
    assert_equal(row.rendered_value,
                 "TEST1                                        TEST2")


def test_row_render_three_columns():
    cell1 = Cell("TEST1", False)
    cell2 = Cell("TEST2", True)
    cell3 = Cell("TEST3", True)
    row = Row([cell1, cell2, cell3], 50)
    row.render()
    assert_equal(row.rendered_value,
                 "TEST1                      TEST2           TEST3")
