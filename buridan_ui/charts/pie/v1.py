import reflex as rx

from ..style import info, tooltip


def piechart_v1():
    data = [
        {"browser": "chrome", "visitors": 275},
        {"browser": "safari", "visitors": 200},
        {"browser": "firefox", "visitors": 187},
        {"browser": "edge", "visitors": 173},
        {"browser": "other", "visitors": 90},
    ]

    data = [
        {**item, "fill": rx.color("accent", index + 4)}
        for index, item in enumerate(data)
    ]

    return rx.vstack(
        info("Pie Chart", "3", "January - June 2024", "center"),
        rx.recharts.pie_chart(
            rx.recharts.graphing_tooltip(**tooltip),
            rx.recharts.pie(
                data=data,
                data_key="visitors",
                name_key="browser",
                stroke="0",
                is_animation_active=False,
            ),
            width="100%",
            height=250,
        ),
        info(
            "Trending up by 5.2% this month",
            "2",
            "Showing total visitors for the last 6 months",
            "center",
        ),
        width="100%",
        align="center",
        padding="0.5em",
        class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
    )
