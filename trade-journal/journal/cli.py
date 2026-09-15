import argparse
from journal.models import Journal
from journal.trade import Trade


def cmd_add(args: argparse.Namespace) -> None:
    journal = Journal()
    trade = Trade(
        direction=args.direction,
        entry_time=args.entry_time,
        r_result=args.result,
    )
    journal.add_trade(trade)
    print(f"Added trade: {trade}")


def cmd_view(args: argparse.Namespace) -> None:
    journal = Journal()
    journal.print_all_trades()


def cmd_stats(args: argparse.Namespace) -> None:
    journal = Journal()
    print(f"Win rate: {journal.win_rate()}%")
    print(f"Expectancy: {journal.expectancy()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Trade Journal CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new trade")
    add_parser.add_argument("--direction", required=True, choices=["long", "short"])
    add_parser.add_argument("--entry-time", required=True, dest="entry_time")
    add_parser.add_argument("--result", required=True, type=int)
    add_parser.set_defaults(func=cmd_add)

    view_parser = subparsers.add_parser("view", help="View all trades")
    view_parser.set_defaults(func=cmd_view)

    stats_parser = subparsers.add_parser("stats", help="Show win rate and expectancy")
    stats_parser.set_defaults(func=cmd_stats)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
