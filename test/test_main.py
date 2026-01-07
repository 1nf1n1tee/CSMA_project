from src import main

def test_sender_runs(capsys):
    main.sender("Alice", "Bob", "HI")
    captured = capsys.readouterr()
    assert "Bob received: H from Alice" in captured.out
    assert "Bob received: I from Alice" in captured.out
    assert "Alice finished sending message to Bob" in captured.out