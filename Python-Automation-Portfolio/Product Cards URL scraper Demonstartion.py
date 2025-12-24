"""
This script demonstrates a production-style Python data scraping
workflow using Python and selenium complex level data scraping to scrap usefull Information.
This is Designed to Handle Cookies popup and scrape Product URLs from all catalogs 
except the skipped ones.

IMPORTANT:
- Real URLS and client data is removed
- Core Scraping logic is abstracted where necessary
- This file is for skill demonstration only
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv, os
from datetime import datetime
import sys
import codecs

if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    
# === OUTPUT FOLDER ===
output_dir = r"Computer's Address"
os.makedirs(output_dir, exist_ok=True)

# === SETUP SELENIUM ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)




#Skipping start

def should_skip_category(catalog_name=None, sub_category_name=None, sub_sub_category_name=None, sub_sub_sub_category_name=None):
    """
    Check if a category should be skipped based on its name.
    Add the exact names you want to skip in the lists below.
    
    Returns True if the category should be skipped, False otherwise.
    """
    
    # List of catalog names to skip (exact matches)
    SKIP_CATALOGS = [
        # Add catalog names to skip here
        # Example: "Brake System",
        # Example: "Engine",
        
    ]
    
    # List of sub-category names to skip (exact matches)
    SKIP_SUB_CATEGORIES = [
        # Add sub-category names to skip here
        # Example: "Brake Discs",
        # Example: "Spark Plugs",

        
    ]
    
    # List of sub-sub-category names to skip (exact matches)
    SKIP_SUB_SUB_CATEGORIES = [
        # Add sub-sub-category names to skip here
        # Example: "Front Brake Discs",
        # Example: "Iridium Spark Plugs",

    ]
    
    # List of sub-sub-sub-category names to skip (exact matches)
    SKIP_SUB_SUB_SUB_CATEGORIES = [
        # Add sub-sub-sub-category names to skip here
        # Example: "Vented Brake Discs",
        # Example: "Laser Iridium Spark Plugs",

    ]
    
    # Check catalog name
    if catalog_name and catalog_name in SKIP_CATALOGS:
        print(f"Skipping catalog: {catalog_name}")
        return True
    
    # Check sub-category name
    if sub_category_name and sub_category_name in SKIP_SUB_CATEGORIES:
        print(f"Skipping sub-category: {sub_category_name}")
        return True
    
    # Check sub-sub-category name
    if sub_sub_category_name and sub_sub_category_name in SKIP_SUB_SUB_CATEGORIES:
        print(f"Skipping sub-sub-category: {sub_sub_category_name}")
        return True
    
    # Check sub-sub-sub-category name
    if sub_sub_sub_category_name and sub_sub_sub_category_name in SKIP_SUB_SUB_SUB_CATEGORIES:
        print(f"Skipping sub-sub-sub-category: {sub_sub_sub_category_name}")
        return True
    
    return False
#skipping End




def get_clean_text(element):
    """Get clean text from an element, trying multiple methods"""
    text = ""
    
    # Try .text first
    try:
        text = element.text.strip()
    except:
        pass
    
    # If empty, try innerText
    if not text:
        try:
            text = element.get_attribute("innerText").strip()
        except:
            pass
    
    # If still empty, try textContent
    if not text:
        try:
            text = element.get_attribute("textContent").strip()
        except:
            pass
    
    # Clean up the text
    if text:
        # Replace multiple spaces/newlines with single space
        text = ' '.join(text.split())
        # Remove any remaining control characters
        text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        text = text.strip()
    
    return text


def collapse_other_expanded_sub_categories(current_sub_category_name):
    """Collapse all other expanded sub-categories except the current one"""
    try:
        # Find all expanded sub-categories (with class containing 'active')
        expanded_sub_categories = driver.find_elements(By.CSS_SELECTOR, 
            "a.catalog-menu__sub-link.catalog-menu__sub-link--parent._js-catalog-menu__item-link.active")
        
        for expanded_category in expanded_sub_categories:
            try:
                # Get the name of this expanded category
                expanded_name = get_clean_text(expanded_category)
                
                
                """
                The Code is Removed Form Here, Because it is jsut Demonstration
                """
            except:
                continue
                
        return True
    except Exception as e:
        print(f"    Error collapsing other sub-categories: {e}")
        return False


def click_safe(elem):
    """Safely click an element with scrolling"""
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", elem)
    try:
        elem.click()
    except:
        driver.execute_script("arguments[0].click();", elem)
    time.sleep(2)

def is_in_catalog_menu():
    """Check if we're in the main catalog menu (not in category menu)"""
    try:
        # Check for "Catalogue" text in catalog menu
                """
                The Code is Removed Form Here, Because it is jsut Demonstration
                """
    except:
        return False

def is_in_category_menu():
    """Check if we're in the category menu (sub-categories view)"""
    try:
        # Check for catalog name in category menu
            """
            The Code is Removed Form Here, Because it is jsut Demonstration
            """
    except:
        return False

def go_back_to_catalog_menu():
    """Click the back button to return to catalog menu from category menu"""
    try:
        back_button = driver.find_element(By.CSS_SELECTOR, "div.catalog-menu__sub-back._js-catalog-menu__sub-back")
            #The Code is Removed Form Here, Because it is jsut Demonstration
        return True
    except:
        print("  Could not find back button")
        return False

def get_product_urls_and_names_from_current_page():
    """Extract product URLs and names from the current listing page"""
    products = []
    try:
        # Try multiple selectors to find product cards
        selectors = [
            # Here a tags selectors Removed
        ]
        
        for selector in selectors:
            try:
                product_cards = driver.find_elements(By.CSS_SELECTOR, selector)
                if product_cards:
                    for card in product_cards:
                        href = card.get_attribute("href")
                        if href and href.strip() and "/product/" in href:
                            # Skip URLs that end with letter "P"
                            if not href.strip().upper().endswith('P'):
                                url = href.strip()
                                
                                # Get product name
                                product_name = ""
                                """
                                The Code is Removed Form Here, Because it is jsut Demonstration
                                """
                                
                                products.append({
                                    "url": url,
                                    "name": product_name
                                })
                    if products:
                        break
            except:
                continue
                
    except Exception as e:
        print(f"Error extracting products: {e}")
    
    return products

def get_all_products_in_category():
    """Get all product URLs and names from all pages of the current category"""
    all_products = []
    page_num = 1
    had_multiple_pages = False
    
    while True:
        print(f"  Processing page {page_num}")
        
        # Get products from current page
        products = get_product_urls_and_names_from_current_page()
        all_products.extend(products)
        
        if products:
            print(f"    Found {len(products)} products on page {page_num}")
        else:
            print(f"    No products found on page {page_num}")
        
        # Check if there's a next page
        try:
            # Find all pagination elements
            pagination_selectors = [
                "div.pagination__item",
                "a.pagination__item-link",
                "li.pagination__item",
                "div.pagination a"
            ]
            
            next_page_found = False
            
            """
            62 Line of Codes are Removed Form Here, Because it is jsut Demonstration
            """
            
            # If no next page found, check for next arrow
            if not next_page_found:
                try:
                    next_arrows = driver.find_elements(By.CSS_SELECTOR, "a[aria-label='Next'], div.pagination__next, a.pagination__next")
                    for arrow in next_arrows:
                        if arrow.is_displayed() and arrow.is_enabled():
                            click_safe(arrow)
                            page_num += 1
                            next_page_found = True
                            had_multiple_pages = True
                            time.sleep(3)
                            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.listing-list")))
                            break
                except:
                    pass
            
            # If still no next page found, break
            if not next_page_found:
                break
                
        except Exception as e:
            print(f"Error checking pagination: {e}")
            break
    
    # REMOVED THE DUPLICATE REMOVAL LOGIC
    # Return all products as-is, including potential duplicates
    return all_products, had_multiple_pages
def open_catalog_menu():
    """Open the catalog menu by clicking the yellow button"""
    try:
        """
            93 Lines of Code Removed Form Here, Because it is jsut Demonstration
        """
    except Exception as e:
        print(f"  Failed to open catalog menu: {e}")
        return False

def process_leaf_category(catalog_name, sub_category_name, sub_sub_category_name=None, sub_sub_sub_category_name=None):
    """Process a leaf category (no further subcategories) and collect product URLs and names"""
    try:
        # Wait for the page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.listing-list, div.listing-content")))
        time.sleep(3)
        
        # Check if there are any product cards
        """
            32 Lines of Code Removed Form Here, Because it is jsut Demonstration
        """
        
        # Get all products from this category
        products, had_multiple_pages = get_all_products_in_category()
        
        if not products:
            print(f"  No products found in this category")
        
        # Prepare data for CSV
        data = []
        """
            15 Lines of Code Removed Form Here, Because it is jsut Demonstration
        """
        
        print(f"  Total products collected: {len(products)}")
        print(f"  Had multiple pages: {had_multiple_pages}")
        
        return data, had_multiple_pages
        
    except Exception as e:
        print(f"Error processing category: {e}")
        return [], True  # Assume we need to reopen catalog on error

def save_catalog_to_csv(catalog_name, catalog_data):
    """Save catalog data to a CSV file"""
    if not catalog_data:
        print(f"No data to save for catalog: {catalog_name}")
        return
    
    # Sanitize filename
    safe_catalog_name = "".join(c for c in catalog_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
    filename = os.path.join(output_dir, f"{safe_catalog_name}.csv")
    
    # Define headers with Sub-Sub-Sub Category and Name columns
    headers = ["Catalog", "Sub Category", "Sub-Sub Category", "Sub-Sub-Sub Category", "URL", "Name"]
    
    # Write to CSV
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(catalog_data)
    
    print(f"Saved {len(catalog_data)} products to {filename}")

def process_sub_sub_sub_categories(catalog_name, sub_category_name, sub_sub_category_name, catalog_items, i, j, parent_index, need_to_reopen_catalog, processed_sub_sub_sub_categories):
    """Process sub-sub-sub categories (4th level)"""
    catalog_data = []
    
    # Get all sub-sub-sub categories - only from visible scroll container
    sub_sub_sub_selectors = [
        "div.catalog-menu__sub-drop.catalog-menu__sub-drop-lvl2 a.catalog-menu__sub-link",
        "div.catalog-menu__sub-drop.catalog-menu__sub-drop-lvl2 div.catalog-menu__sub-item a",
        "div.catalog-menu__sub-drop-lvl2 a.catalog-menu__sub-link"
    ]
    
    sub_sub_sub_items = []
    for selector in sub_sub_sub_selectors:
        """
            118 Lines of Code Removed Form Here, Because it is jsut Demonstration
        """
    
    print(f"    Found {len(sub_sub_sub_items)} sub-sub-sub categories (level 5)")
    
    # Process each sub-sub-sub category
    for k in range(len(sub_sub_sub_items)):
        try:
            # If we need to reopen catalog menu, do it now
            if need_to_reopen_catalog:
                print(f"      Need to reopen catalog menu for next sub-sub-sub category")
                open_catalog_menu()
                time.sleep(2)
                
                # Check if we're in category menu, go back to catalog menu if needed
                if is_in_category_menu():
                    go_back_to_catalog_menu()
                    time.sleep(2)
                
                # Reselect the catalog
                catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                if i < len(catalog_items):
                    click_safe(catalog_items[i])
                    time.sleep(2)
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.catalog-menu__sub.show, div.catalog-menu__sub._js-catalog-menu__sub")))
                    time.sleep(2)
                    
                    """
                        62 Lines of Code Removed Form Here, Because it is jsut Demonstration
                    """
            
            # Refresh sub-sub-sub items - only from visible containers
            sub_sub_sub_items = []
            """
            67 Lines of Code Removed Form Here, Because it is jsut Demonstration
            """
                    
            if k >= len(sub_sub_sub_items):
                break
                
            sub_sub_sub_item = sub_sub_sub_items[k]
            sub_sub_sub_category_name = get_clean_text(sub_sub_sub_item)
            if not sub_sub_sub_category_name or len(sub_sub_sub_category_name) < 2:
                sub_sub_sub_category_name = f"Sub_Sub_Sub_Category_{k+1}"
            
            # Check if we've already processed this sub-sub-sub category
            if sub_sub_sub_category_name in processed_sub_sub_sub_categories:
                print(f"      Skipping sub-sub-sub category {sub_sub_sub_category_name} - already processed")
                continue
                
            # Mark as processed
            processed_sub_sub_sub_categories.add(sub_sub_sub_category_name)
            
            print(f"      Processing sub-sub-sub category {k+1}/{len(sub_sub_sub_items)}: {sub_sub_sub_category_name}")
            
            # Click on sub-sub-sub category
            click_safe(sub_sub_sub_item)
            
            # Collect products
            sub_data, had_multiple_pages = process_leaf_category(
                catalog_name, 
                sub_category_name, 
                sub_sub_category_name,
                sub_sub_sub_category_name
            )
            catalog_data.extend(sub_data)
            
            # Update need_to_reopen_catalog based on whether we had multiple pages
            if had_multiple_pages:
                need_to_reopen_catalog = True
            else:
                driver.back()
                time.sleep(3)
                need_to_reopen_catalog = False
            
        except Exception as e:
            print(f"      Error processing sub-sub-sub category: {e}")
            need_to_reopen_catalog = True
            continue
    
    return catalog_data, need_to_reopen_catalog, processed_sub_sub_sub_categories

def main():
    try:
        # 1. Open site
        print("Website Name")
        driver.get("https://www.WebsiteName.eu/")
        
        # 2. Select English language
        try:
            english_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='name' and normalize-space()='English']")))
            click_safe(english_btn)
            print("Language set to English")
            time.sleep(3)
        except:
            print("Could not find language selector, continuing...")
        
        # 3. Accept cookies if present
        try:
            cookie_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div._js-cookies-accept-all, button._js-cookies-accept-all")))
            click_safe(cookie_btn)
            print("Cookies accepted")
            time.sleep(2)
        except:
            print("No cookie banner found, continuing...")
        
        # 4. Open the catalog menu for the first time
        print("Opening catalog menu...")
        open_catalog_menu()
        
        # 5. Get all catalog items
        catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
        print(f"Found {len(catalog_items)} catalogs")
        
        # Process each catalog
        for i in range(len(catalog_items)):
            try:
                # Refresh catalog items list at the start of each iteration
                # This prevents stale element references
                time.sleep(1)
                catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                
                """
                    59 Lines of Code Removed Form Here, Because it is jsut Demonstration
                """
                
                # Clean up the catalog name
                if catalog_name:
                    catalog_name = ' '.join(catalog_name.split())
                    catalog_name = catalog_name.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
                    catalog_name = catalog_name.strip()
                    
                    # Extract text inside double quotes if present
                    import re
                    match = re.search(r'"([^"]*)"', catalog_name)
                    if match:
                        catalog_name = match.group(1).strip()
                
                # If still no valid name, use default
                if not catalog_name or len(catalog_name) < 2:
                    catalog_name = f"Catalog_{i+1}"
                
                print(f"\n{'='*60}")
                print(f"Processing catalog {i+1}/{len(catalog_items)}: {catalog_name}")
                print('='*60)
                
                """
                    45 Lines of Code Removed Form Here, Because it is jsut Demonstration
                """
                # Get fresh reference again after navigation
                catalog_item = catalog_items[i]
                
                # Debug: Print what we're clicking on
                try:
                    item_text = get_clean_text(catalog_item)
                    print(f"  Clicking on catalog item with text: {item_text}")
                except:
                    pass
                    
                # Click on the catalog
                print(f"Clicking on catalog: {catalog_name}")
                click_safe(catalog_item)
                time.sleep(2)
                
                # Wait for sub-categories to appear
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.catalog-menu__sub.show, div.catalog-menu__sub._js-catalog-menu__sub")))
                time.sleep(2)
                
                # Get all sub-categories - only from visible scroll container and check data-level=3
                sub_selectors = [
                    "a.catalog-menu__sub-link",
                    "a.catalog-menu__sub-link._js-catalog-menu__item-link",
                    "div.catalog-menu__sub-item a"
                ]
                
                sub_category_items = []
                for selector in sub_selectors:
                    try:
                        # Only get items from visible containers (not display: none)
                        all_items = driver.find_elements(By.CSS_SELECTOR, selector)
                        for item in all_items:
                            # Check if parent container is visible (not display: none)
                            try:
                                scroll_container = item.find_element(By.XPATH, ".//ancestor::div[contains(@class, 'catalog-menu__scroll')]")
                                style_attr = scroll_container.get_attribute("style")
                                if not style_attr or "display: none" not in style_attr:
                                    # Check data-level attribute to ensure it's level 3 (sub-category)
                                    data_level = item.get_attribute("data-level")
                                    if data_level == "3":
                                        sub_category_items.append(item)
                            except:
                                # If can't find scroll container or data-level, skip this item
                                continue
                        if sub_category_items:
                            print(f"Found {len(sub_category_items)} sub-categories (level 3) using selector: {selector}")
                            break
                    except:
                        continue
                
                """
                99 Lines of Code Removed Form Here, Because it is jsut Demonstration
                """
                
                if not sub_category_items:
                    print("Skipping catalog - no sub-categories found")
                    # Go back to catalog menu for next catalog
                    if is_in_category_menu():
                        go_back_to_catalog_menu()
                    continue
                
                catalog_data = []
                need_to_reopen_catalog = False  # Track if we need to reopen catalog menu
                
                # Track processed categories by name (not just index)
                processed_sub_categories = set()  # Level 3
                processed_sub_sub_categories = set()  # Level 4
                
                # Process each sub-category
                j = 0
                while j < len(sub_category_items):
                    try:
                        # If we need to reopen catalog menu, do it now
                        if need_to_reopen_catalog:
                            print(f"  Need to reopen catalog menu for next sub-category")
                            open_catalog_menu()
                            time.sleep(2)
                            
                            # Check if we're in category menu, go back to catalog menu if needed
                            if is_in_category_menu():
                                go_back_to_catalog_menu()
                                time.sleep(2)
                            
                            # Reselect the catalog
                            catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                            if i < len(catalog_items):
                                click_safe(catalog_items[i])
                                time.sleep(2)
                                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.catalog-menu__sub.show, div.catalog-menu__sub._js-catalog-menu__sub")))
                                time.sleep(2)
                        
                        # Refresh the sub-category items list - only from visible containers and check data-level=3
                        sub_category_items = []
                        for selector in sub_selectors:
                            try:
                                all_items = driver.find_elements(By.CSS_SELECTOR, selector)
                                for item in all_items:
                                    # Check if parent container is visible (not display: none)
                                    try:
                                        scroll_container = item.find_element(By.XPATH, ".//ancestor::div[contains(@class, 'catalog-menu__scroll')]")
                                        style_attr = scroll_container.get_attribute("style")
                                        if not style_attr or "display: none" not in style_attr:
                                            # Check data-level attribute to ensure it's level 3 (sub-category)
                                            data_level = item.get_attribute("data-level")
                                            if data_level == "3":
                                                sub_category_items.append(item)
                                    except:
                                        # If can't find scroll container or data-level, skip this item
                                        continue
                                if sub_category_items:
                                    break
                            except:
                                continue
                                
                        if j >= len(sub_category_items):
                            break
                            
                        sub_item = sub_category_items[j]
                        sub_category_name = get_clean_text(sub_item)
                        if not sub_category_name or len(sub_category_name) < 2:
                            sub_category_name = f"Sub_Category_{j+1}"
                        
                        # Check if we've already processed this sub-category
                        if sub_category_name in processed_sub_categories:
                            print(f"  Skipping sub-category {sub_category_name} - already processed")
                            j += 1
                            continue
                        
                        # Mark as processed
                        processed_sub_categories.add(sub_category_name)
                        
                        print(f"\n  Processing sub-category {j+1}/{len(sub_category_items)}: {sub_category_name}")
                        
                        # Check if this sub-category has further sub-sub-categories
                        item_classes = sub_item.get_attribute("class")
                        has_sub_sub = "catalog-menu__sub-link--parent" in item_classes
                        
                        if has_sub_sub:
                            print(f"    This sub-category has sub-sub-categories")
                            
                            # Click to expand sub-sub-categories
                            click_safe(sub_item)
                            time.sleep(2)
                            
                            # Collapse any other expanded sub-categories to avoid confusion
                            collapse_other_expanded_sub_categories(sub_category_name)
                            
                            # Wait for sub-sub-categories to appear
                            try:
                                wait.until(EC.presence_of_element_located((
                                    By.CSS_SELECTOR, 
                                    "div.catalog-menu__sub-drop[style*='display: block'], div.catalog-menu__sub-drop._js-catalog-menu__sub-drop"
                                )))
                            except:
                                print("    Could not find sub-sub-categories dropdown")
                                j += 1
                                continue
                            
                            # Get all sub-sub-categories - only from visible scroll container and check data-level=4
                            sub_sub_selectors = [
                                "div.catalog-menu__sub-drop[style*='display: block'] a.catalog-menu__sub-link",
                                "div.catalog-menu__sub-drop a.catalog-menu__sub-link",
                                "div.catalog-menu__sub-drop div.catalog-menu__sub-item a"
                            ]
                            
                            sub_sub_items = []
                            """
                                64 Lines of Code Removed Form Here, Because it is jsut Demonstration
                            """
                            
                            print(f"    Found {len(sub_sub_items)} sub-sub-categories (level 4)")
                            
                        
                            
                            # Process each sub-sub-category
                            for k in range(len(sub_sub_items)):
                                try:
                                    # If we need to reopen catalog menu, do it now
                                    if need_to_reopen_catalog:
                                        print(f"      Need to reopen catalog menu for next sub-sub-category")
                                        open_catalog_menu()
                                        time.sleep(2)
                                        
                                        # Check if we're in category menu, go back to catalog menu if needed
                                        if is_in_category_menu():
                                            go_back_to_catalog_menu()
                                            time.sleep(2)
                                        
                                        # Reselect the catalog
                                        catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                                        if i < len(catalog_items):
                                            click_safe(catalog_items[i])
                                            time.sleep(2)
                                            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.catalog-menu__sub.show, div.catalog-menu__sub._js-catalog-menu__sub")))
                                            time.sleep(2)
                                            
                                            # Re-expand the parent sub-category
                                            sub_category_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__sub-link, a.catalog-menu__sub-link._js-catalog-menu__item-link")
                                            if j < len(sub_category_items):
                                                parent_item = sub_category_items[j]
                                                if "catalog-menu__sub-link--parent" in parent_item.get_attribute("class"):
                                                    click_safe(parent_item)
                                                    time.sleep(2)
                                                    
                                                    # Collapse any other expanded sub-categories
                                                    collapse_other_expanded_sub_categories(sub_category_name)
                                    
                                    # Refresh sub-sub items - only from visible containers and check data-level=4
                                    sub_sub_items = []
                                    for selector in sub_sub_selectors:
                                        try:
                                            all_items = driver.find_elements(By.CSS_SELECTOR, selector)
                                            for item in all_items:
                                                # Check if parent container is visible (not display: none)
                                                try:
                                                    scroll_container = item.find_element(By.XPATH, ".//ancestor::div[contains(@class, 'catalog-menu__scroll')]")
                                                    style_attr = scroll_container.get_attribute("style")
                                                    if not style_attr or "display: none" not in style_attr:
                                                        # Check data-level attribute to ensure it's level 4 (sub-sub-category)
                                                        data_level = item.get_attribute("data-level")
                                                        if data_level == "4":
                                                            sub_sub_items.append(item)
                                                except:
                                                    # If can't find scroll container or data-level, skip this item
                                                    continue
                                            if sub_sub_items:
                                                break
                                        except:
                                            continue
                                            
                                    if k >= len(sub_sub_items):
                                        break
                                        
                                    sub_sub_item = sub_sub_items[k]
                                    sub_sub_category_name = get_clean_text(sub_sub_item)
                                    """
                                    178 Lines of Code Removed Form Here, Because it is jsut Demonstration
                                    """
                                        
                                        # Update need_to_reopen_catalog based on whether we had multiple pages
                                    
                                except Exception as e:
                                    print(f"      Error processing sub-sub-category: {e}")
                                    need_to_reopen_catalog = True
                                    continue
                            
                            # After processing all sub-sub-categories, increment j to move to next sub-category
                            j += 1
                            
                        else:
                            # This is a leaf sub-category without further sub-sub-categories
                            print(f"    This is a leaf sub-category")
                            
                            # Click on sub-category
                            click_safe(sub_item)
                            
                            # Collect products
                            sub_data, had_multiple_pages = process_leaf_category(
                                catalog_name, 
                                sub_category_name
                            )
                            catalog_data.extend(sub_data)
                            
                            # Update need_to_reopen_catalog based on whether we had multiple pages
                            if had_multiple_pages:
                                need_to_reopen_catalog = True
                            else:
                                driver.back()
                                time.sleep(3)
                                need_to_reopen_catalog = False
                            
                            j += 1
                            
                    except Exception as e:
                        print(f"  Error processing sub-category: {e}")
                        need_to_reopen_catalog = True  # Assume error means we need to reopen
                        j += 1  # Move to next sub-category even on error
                        continue
                
                # Save catalog data to CSV
                save_catalog_to_csv(catalog_name, catalog_data)
                
                # For next catalog, we need to go back to catalog menu
                # If we're in category menu, click the back button
                if is_in_category_menu():
                    print("  Going back to catalog menu for next catalog...")
                    go_back_to_catalog_menu()
                    time.sleep(2)
                
                # Refresh catalog items list for next catalog
                catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                
            except Exception as e:
                print(f"Error processing catalog: {e}")
                # Try to recover by going back to catalog menu
                try:
                    if is_in_category_menu():
                        go_back_to_catalog_menu()
                    else:
                        open_catalog_menu()
                    time.sleep(2)
                    catalog_items = driver.find_elements(By.CSS_SELECTOR, "a.catalog-menu__item-link._js-catalog-menu__item-link._js-gtm-categories-item")
                except:
                    pass
                continue
        
        print("\n" + "="*60)
        print("All catalogs processed successfully!")
        print("="*60)
        
    except Exception as e:
        print(f"Script failed: {e}")
        import traceback
        traceback.print_exc()
        # Save error information
        try:
            with open(os.path.join(output_dir, "error.html"), "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            driver.save_screenshot(os.path.join(output_dir, "error.png"))
            print("Error details saved to output folder")
        except:
            pass
    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
