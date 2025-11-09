from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    TextColumn,
    TimeElapsedColumn,
)


def progress(note: str = "processing"):
    return Progress(
        TextColumn(f"{note} •" + "[progress.percentage]{task.percentage:>3.0f}%"),
        BarColumn(),
        MofNCompleteColumn(),
        TextColumn("•"),
        TimeElapsedColumn(),
    )

def download_all_datasets():
    from evalplus.data.humaneval import get_human_eval_plus
    from evalplus.data.mbpp import get_mbpp_plus

    get_human_eval_plus()
    get_mbpp_plus()    

if __name__ == "__main__":
    download_all_datasets()