import reflex as rx

from ..style import info, tooltip


def areachart_v5():
    from reflex.experimental import ClientStateVar

    data = [
        {"date": "Apr 01", "desktop": 222, "mobile": 150},
        {"date": "Apr 02", "desktop": 97, "mobile": 180},
        {"date": "Apr 03", "desktop": 167, "mobile": 120},
        {"date": "Apr 04", "desktop": 242, "mobile": 260},
        {"date": "Apr 05", "desktop": 373, "mobile": 290},
        {"date": "Apr 06", "desktop": 301, "mobile": 340},
        {"date": "Apr 07", "desktop": 245, "mobile": 180},
        {"date": "Apr 08", "desktop": 409, "mobile": 320},
        {"date": "Apr 09", "desktop": 59, "mobile": 110},
        {"date": "Apr 10", "desktop": 261, "mobile": 190},
        {"date": "Apr 11", "desktop": 327, "mobile": 350},
        {"date": "Apr 12", "desktop": 292, "mobile": 210},
        {"date": "Apr 13", "desktop": 342, "mobile": 380},
        {"date": "Apr 14", "desktop": 137, "mobile": 220},
        {"date": "Apr 15", "desktop": 120, "mobile": 170},
        {"date": "Apr 16", "desktop": 138, "mobile": 190},
        {"date": "Apr 17", "desktop": 446, "mobile": 360},
        {"date": "Apr 18", "desktop": 364, "mobile": 410},
        {"date": "Apr 19", "desktop": 243, "mobile": 180},
        {"date": "Apr 20", "desktop": 89, "mobile": 150},
        {"date": "Apr 21", "desktop": 137, "mobile": 200},
        {"date": "Apr 22", "desktop": 224, "mobile": 170},
        {"date": "Apr 23", "desktop": 138, "mobile": 230},
        {"date": "Apr 24", "desktop": 387, "mobile": 290},
        {"date": "Apr 25", "desktop": 215, "mobile": 250},
        {"date": "Apr 26", "desktop": 75, "mobile": 130},
        {"date": "Apr 27", "desktop": 383, "mobile": 420},
        {"date": "Apr 28", "desktop": 122, "mobile": 180},
        {"date": "Apr 29", "desktop": 315, "mobile": 240},
        {"date": "Apr 30", "desktop": 454, "mobile": 380},
        {"date": "May 01", "desktop": 165, "mobile": 220},
        {"date": "May 02", "desktop": 293, "mobile": 310},
        {"date": "May 03", "desktop": 247, "mobile": 190},
        {"date": "May 04", "desktop": 385, "mobile": 420},
        {"date": "May 05", "desktop": 481, "mobile": 390},
        {"date": "May 06", "desktop": 498, "mobile": 520},
        {"date": "May 07", "desktop": 388, "mobile": 300},
        {"date": "May 08", "desktop": 149, "mobile": 210},
        {"date": "May 09", "desktop": 227, "mobile": 180},
        {"date": "May 10", "desktop": 293, "mobile": 330},
        {"date": "May 11", "desktop": 335, "mobile": 270},
        {"date": "May 12", "desktop": 197, "mobile": 240},
        {"date": "May 13", "desktop": 197, "mobile": 160},
        {"date": "May 14", "desktop": 448, "mobile": 490},
        {"date": "May 15", "desktop": 473, "mobile": 380},
        {"date": "May 16", "desktop": 338, "mobile": 400},
        {"date": "May 17", "desktop": 499, "mobile": 420},
        {"date": "May 18", "desktop": 315, "mobile": 350},
        {"date": "May 19", "desktop": 235, "mobile": 180},
        {"date": "May 20", "desktop": 177, "mobile": 230},
        {"date": "May 21", "desktop": 82, "mobile": 140},
        {"date": "May 22", "desktop": 81, "mobile": 120},
        {"date": "May 23", "desktop": 252, "mobile": 290},
        {"date": "May 24", "desktop": 294, "mobile": 220},
        {"date": "May 25", "desktop": 201, "mobile": 250},
        {"date": "May 26", "desktop": 213, "mobile": 170},
        {"date": "May 27", "desktop": 420, "mobile": 460},
        {"date": "May 28", "desktop": 233, "mobile": 190},
        {"date": "May 29", "desktop": 78, "mobile": 130},
        {"date": "May 30", "desktop": 340, "mobile": 280},
        {"date": "May 31", "desktop": 178, "mobile": 230},
        {"date": "Jun 01", "desktop": 178, "mobile": 200},
        {"date": "Jun 02", "desktop": 470, "mobile": 410},
        {"date": "Jun 03", "desktop": 103, "mobile": 160},
        {"date": "Jun 04", "desktop": 439, "mobile": 380},
        {"date": "Jun 05", "desktop": 88, "mobile": 140},
        {"date": "Jun 06", "desktop": 294, "mobile": 250},
        {"date": "Jun 07", "desktop": 323, "mobile": 370},
        {"date": "Jun 08", "desktop": 385, "mobile": 320},
        {"date": "Jun 09", "desktop": 438, "mobile": 480},
        {"date": "Jun 10", "desktop": 155, "mobile": 200},
        {"date": "Jun 11", "desktop": 92, "mobile": 150},
        {"date": "Jun 12", "desktop": 492, "mobile": 420},
        {"date": "Jun 13", "desktop": 81, "mobile": 130},
        {"date": "Jun 14", "desktop": 426, "mobile": 380},
        {"date": "Jun 15", "desktop": 307, "mobile": 350},
        {"date": "Jun 16", "desktop": 371, "mobile": 310},
        {"date": "Jun 17", "desktop": 475, "mobile": 520},
        {"date": "Jun 18", "desktop": 107, "mobile": 170},
        {"date": "Jun 19", "desktop": 341, "mobile": 290},
        {"date": "Jun 20", "desktop": 408, "mobile": 450},
        {"date": "Jun 21", "desktop": 169, "mobile": 210},
        {"date": "Jun 22", "desktop": 317, "mobile": 270},
        {"date": "Jun 23", "desktop": 480, "mobile": 530},
        {"date": "Jun 24", "desktop": 132, "mobile": 180},
        {"date": "Jun 25", "desktop": 141, "mobile": 190},
        {"date": "Jun 26", "desktop": 434, "mobile": 380},
        {"date": "Jun 27", "desktop": 448, "mobile": 490},
        {"date": "Jun 28", "desktop": 149, "mobile": 200},
        {"date": "Jun 29", "desktop": 103, "mobile": 160},
        {"date": "Jun 30", "desktop": 446, "mobile": 400},
    ]

    SelectedRange = ClientStateVar.create("selected", data)

    return rx.center(
        rx.vstack(
            rx.hstack(
                info(
                    "Area Chart - Dynamic",
                    "3",
                    "Showing total visitors for the last 6 months",
                    "start",
                ),
                rx.el.select(
                    rx.el.option(
                        "Last 3 Months", on_click=SelectedRange.set_value(data)
                    ),
                    rx.el.option(
                        "Last 30 days", on_click=SelectedRange.set_value(data[-30:])
                    ),
                    rx.el.option(
                        "Last 7 days", on_click=SelectedRange.set_value(data[-7:])
                    ),
                    default_value="Last 3 months",
                    bg=rx.color("gray", 2),
                    border=f"1px solid {rx.color('gray', 4)}",
                    class_name="relative flex items-center whitespace-nowrap justify-center gap-2 py-2 rounded-lg shadow-sm px-3",
                ),
                align="center",
                justify="between",
                width="100%",
                wrap="wrap",
            ),
            rx.recharts.area_chart(
                rx.el.svg.defs(
                    rx.el.svg.linear_gradient(
                        rx.el.svg.stop(
                            stop_color=rx.color("accent", 7),
                            offset="0%",
                            stop_opacity=0.3,
                        ),
                        rx.el.svg.stop(
                            stop_color=rx.color("accent", 8),
                            offset="95%",
                            stop_opacity=0.1,
                        ),
                        x1=0,
                        x2=0,
                        y1=0,
                        y2=1,
                        id="desktop",
                    )
                ),
                rx.el.svg.defs(
                    rx.el.svg.linear_gradient(
                        rx.el.svg.stop(
                            stop_color=rx.color("orange", 7),
                            offset="0%",
                            stop_opacity=0.3,
                        ),
                        rx.el.svg.stop(
                            stop_color=rx.color("orange", 8),
                            offset="95%",
                            stop_opacity=0.1,
                        ),
                        x1=0,
                        x2=0,
                        y1=0,
                        y2=1,
                        id="mobile",
                    )
                ),
                rx.recharts.graphing_tooltip(**tooltip),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                ),
                *[
                    rx.recharts.area(
                        data_key=name,
                        fill=f"url(#{name})",
                        stack_id="a",
                        stroke=rx.cond(
                            name == "desktop",
                            rx.color("accent", 8),
                            rx.color("orange", 8),
                        ),
                        animation_easing="linear",
                    )
                    for index, name in enumerate(["desktop", "mobile"])
                ],
                rx.recharts.x_axis(
                    data_key="date",
                    axis_line=False,
                    min_tick_gap=32,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=SelectedRange.value,
                width="100%",
                height=280,
            ),
            info(
                "Trending up by 5.2% this month",
                "2",
                "January - June 2024",
                "start",
            ),
            class_name="w-[100%] [&_.recharts-tooltip-item-separator]:w-full",
        ),
        class_name="w-[100%] p-1",
    )
