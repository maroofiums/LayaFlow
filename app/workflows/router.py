from app.decisions.models import Category

CATEGORY_TEAMS = {
    Category.technical: "engineering",
    Category.billing: "billing",
    Category.account: "account_support",
    Category.security:"security",
    Category.general: "general_support",
}


def get_team(category: Category) -> str:
    return CATEGORY_TEAMS[category]