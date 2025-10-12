from dataclasses import dataclass
from typing import Any

@dataclass
class UI:
    """Creates a UI configuration object based on the provided theme and optional parameters

    @param theme: The theme object
    @returns: A partial VSCodeThemeColors object representing the UI configuration.
    """

    theme: Any
    accent: str = "#7D4200"
    accent_lighter: str = "#AA5800"
    accent_tertiary: str = "#EC7900"
    border: str = "#000000"
    border_lighter: str = "#000000"
    border_darker: str = "#000000"
    foreground: str = "#CCCCCC"
    foreground_lighter: str = "#FFFFFF"
    foreground_darker: str = "#555555"
    background: str = "#202126"
    background_lighter: str = "#3c3c3c"
    background_darker: str = "#171717"

    def __init__(self, theme):
        """_summary_

        Args:
            theme (ThemeConfig): _description_
        """
        self.theme = theme

    def build(self):
        return {
            **self.activityBarColors(),
            **self.badgeColors(),
            **self.bannerColors(),
            **self.breadcrumbColors(),
            **self.buttonColors(),
            **self.chartColors(),
            **self.chatColors(),
            **self.checkboxColors(),
            **self.commandCenterColors(),
            **self.commentsViewColors(),
            **self.contrastColors(),
            **self.debugColors(),
            **self.descriptionColors(),
            **self.diffEditorColors(),
            **self.disabledColors(),
            **self.dropdownColors(),
            **self.editorColors(),
            **self.errorColors(),
            **self.extensionColors(),
            **self.gaugeColors(),
            **self.generalColors(),
            **self.gitColors(),
            **self.inlineColors(),
            **self.inputColors(),
            **self.inputOptionColors(),
            **self.inputValidationColors(),
            **self.interactiveColors(),
            **self.issuesColors(),
            **self.keyBindingColors(),
            **self.listColors(),
            **self.menuColors(),
            **self.mergeColors(),
            **self.minimapColors(),
            **self.multiDiffEditorColors(),
            **self.notebookColors(),
            **self.notificationsColors(),
            **self.outputViewColors(),
            **self.panelColors(),
            **self.peekViewColors(),
            **self.pickerGroupColors(),
            **self.portsColors(),
            **self.problemsColors(),
            **self.profileColors(),
            **self.progressBarColors(),
            **self.pullRequestsColors(),
            **self.quickInputColors(),
            **self.radioColors(),
            **self.sashColors(),
            **self.scmGraphColors(),
            **self.scrollBarColors(),
            **self.searchColors(),
            **self.selectionColors(),
            **self.settingsColors(),
            **self.sideBarColors(),
            **self.statusBarColors(),
            **self.symbolIconsColors(),
            **self.tabColors(),
            **self.terminalColors(),
            **self.testingColors(),
            **self.textColors(),
            **self.titleBarColors(),
            **self.toolbarColors(),
            **self.treeColors(),
            **self.walkThroughColors(),
            **self.welcomePageColors(),
            **self.widgetColors(),
            **self.windowColors(),
        }

    def activityBarColors(self):
        return {
            "actionBar.toggledBackground": self.background_darker,
            "activityBar.activeBackground": self.accent,
            "activityBar.activeBorder": self.accent_tertiary,
            "activityBar.activeFocusBorder": self.border,
            "activityBar.background": self.background,
            "activityBar.border": self.border,
            "activityBar.dropBorder": self.border,
            "activityBar.foreground": self.foreground,
            "activityBar.inactiveForeground": self.foreground_darker,
            "activityBarBadge.background": self.accent,
            "activityBarBadge.foreground": self.foreground_lighter,
            "activityBarTop.activeBackground": self.background,
            "activityBarTop.activeBorder": self.border,
            "activityBarTop.background": self.background_darker,
            "activityBarTop.dropBorder": self.border,
            "activityBarTop.foreground": self.foreground,
            "activityBarTop.inactiveForeground": self.foreground_darker,
            # "activityErrorBadge.background": "#000000",
            "activityErrorBadge.foreground": self.foreground_lighter,
            # "activityWarningBadge.background": "#000000",
            "activityWarningBadge.foreground": self.foreground_lighter,
        }

    def badgeColors(self):
        return {
            "badge.background": self.accent,
            "badge.foreground": self.foreground_lighter,
        }

    def bannerColors(self):
        return {
            "banner.background": self.background,
            "banner.foreground": self.foreground,
            "banner.iconForeground": self.foreground_lighter,
        }

    def breadcrumbColors(self):
        return {
            "breadcrumb.activeSelectionForeground": self.foreground_lighter,
            "breadcrumb.background": self.background,
            "breadcrumb.focusForeground": self.foreground_lighter,
            "breadcrumb.foreground": self.foreground,
            "breadcrumbPicker.background": self.background_darker,
        }

    def buttonColors(self):
        return {
            "button.background": self.accent,
            "button.border": self.accent,
            "button.foreground": self.foreground_lighter,
            "button.hoverBackground": self.accent_lighter,
            "button.secondaryBackground": "#3a3d41",
            "button.secondaryForeground": self.foreground_lighter,
            "button.secondaryHoverBackground": "#45494e",
            "button.separator": self.foreground_darker,
        }

    def chartColors(self):
        return {
            # "chart.axis": "#000000",
            # "chart.guide": "#000000",
            # "chart.line": "#000000",
            # "charts.blue": "#000000",
            # "charts.foreground": "#000000",
            # "charts.green": "#000000",
            # "charts.lines": "#000000",
            # "charts.orange": "#000000",
            # "charts.purple": "#000000",
            # "charts.red": "#000000",
            # "charts.yellow": "#000000",
        }

    def chatColors(self):
        return {
            # "chat.avatarBackground": "#000000",
            # "chat.avatarForeground": "#000000",
            # "chat.editedFileForeground": "#000000",
            # "chat.requestBackground": "#000000",
            # "chat.requestBorder": self.border,
            # "chat.slashCommandBackground": "#000000",
            # "chat.slashCommandForeground": "#000000",
        }

    def checkboxColors(self):
        return {
            "checkbox.background": self.background_lighter,
            "checkbox.border": self.border,
            "checkbox.foreground": self.foreground,
            "checkbox.selectBackground": self.background_lighter,
            "checkbox.selectBorder": self.foreground_darker,
        }

    def commandCenterColors(self):
        return {
            # "commandCenter.activeBackground": "#000000",
            # "commandCenter.activeBorder": "#000000",
            # "commandCenter.activeForeground": "#000000",
            # "commandCenter.background": "#000000",
            # "commandCenter.border": "#000000",
            # "commandCenter.debuggingBackground": "#000000",
            # "commandCenter.foreground": "#000000",
            # "commandCenter.inactiveBorder": "#000000",
            # "commandCenter.inactiveForeground": "#000000",
        }

    def commentsViewColors(self):
        return {
            # "commentsView.resolvedIcon": "#000000",
            # "commentsView.unresolvedIcon": "#000000",
        }

    def contrastColors(self):
        return {
            # "contrastActiveBorder": "#000000",
            # "contrastBorder": "#000000",
        }

    def debugColors(self):
        return {
            # "debugConsole.errorForeground": "#000000",
            # "debugConsole.infoForeground": "#000000",
            # "debugConsole.sourceForeground": "#000000",
            # "debugConsole.warningForeground": "#000000",
            # "debugConsoleInputIcon.foreground": "#000000",
            # "debugExceptionWidget.background": "#000000",
            # "debugExceptionWidget.border": "#000000",
            # "debugIcon.breakpointCurrentStackframeForeground": "#000000",
            # "debugIcon.breakpointDisabledForeground": "#000000",
            # "debugIcon.breakpointForeground": "#000000",
            # "debugIcon.breakpointStackframeForeground": "#000000",
            # "debugIcon.breakpointUnverifiedForeground": "#000000",
            # "debugIcon.continueForeground": "#000000",
            # "debugIcon.disconnectForeground": "#000000",
            # "debugIcon.pauseForeground": "#000000",
            # "debugIcon.restartForeground": "#000000",
            # "debugIcon.startForeground": "#000000",
            # "debugIcon.stepBackForeground": "#000000",
            # "debugIcon.stepIntoForeground": "#000000",
            # "debugIcon.stepOutForeground": "#000000",
            # "debugIcon.stepOverForeground": "#000000",
            # "debugIcon.stopForeground": "#000000",
            # "debugTokenExpression.boolean": "#000000",
            # "debugTokenExpression.error": "#000000",
            # "debugTokenExpression.name": "#000000",
            # "debugTokenExpression.number": "#000000",
            # "debugTokenExpression.string": "#000000",
            # "debugTokenExpression.type": "#000000",
            # "debugTokenExpression.value": "#000000",
            # "debugToolBar.background": "#000000",
            # "debugToolBar.border": "#000000",
            # "debugView.exceptionLabelBackground": "#000000",
            # "debugView.exceptionLabelForeground": "#000000",
            # "debugView.stateLabelBackground": "#000000",
            # "debugView.stateLabelForeground": "#000000",
            # "debugView.valueChangedHighlight": "#000000",
        }

    def descriptionColors(self):
        return {
            # "descriptionForeground": "#000000"
            }

    def diffEditorColors(self):
        return {
            "diffEditor.border": "#444444",
            # "diffEditor.diagonalFill": "#000000",
            # "diffEditor.insertedLineBackground": "#000000",
            "diffEditor.insertedTextBackground": "#9bb95533",
            # "diffEditor.insertedTextBorder": "#000000",
            # "diffEditor.move.border": "#000000",
            # "diffEditor.moveActive.border": "#000000",
            # "diffEditor.removedLineBackground": "#000000",
            "diffEditor.removedTextBackground": "#ff000033",
            # "diffEditor.removedTextBorder": "#000000",
            # "diffEditor.unchangedCodeBackground": "#000000",
            # "diffEditor.unchangedRegionBackground": "#000000",
            # "diffEditor.unchangedRegionForeground": "#000000",
            # "diffEditor.unchangedRegionShadow": "#000000",
            # "diffEditorGutter.insertedLineBackground": "#000000",
            # "diffEditorGutter.removedLineBackground": "#000000",
            # "diffEditorOverview.insertedForeground": "#000000",
            # "diffEditorOverview.removedForeground": "#000000",
        }

    def disabledColors(self):
        return {
            "disabledForeground": self.foreground_darker,
        }

    def dropdownColors(self):
        return {
            "dropdown.background": self.background_lighter,
            "dropdown.border": self.border,
            "dropdown.foreground": self.foreground,
            "dropdown.listBackground": self.background_darker,
        }

    def editorColors(self):
        return {
            "editor.background": self.background_darker,
            # "editor.compositionBorder": "#000000",
            "editor.findMatchBackground": "#515c6a",
            "editor.findMatchBorder": "#74879f",
            # "editor.findMatchForeground": "#000000",
            "editor.findMatchHighlightBackground": "#ea5c0055",
            "editor.findMatchHighlightBorder": "#ffffff00",
            # "editor.findMatchHighlightForeground": "#000000",
            "editor.findRangeHighlightBackground": "#3a3d4166",
            "editor.findRangeHighlightBorder": "#ffffff00",
            # "editor.focusedStackFrameHighlightBackground": "#000000",
            # "editor.foldBackground": "#000000",
            # "editor.foldPlaceholderForeground": "#000000",
            "editor.foreground": self.foreground,
            "editor.hoverHighlightBackground": "#264f7840",
            "editor.inactiveSelectionBackground": "#55555599",
            # "editor.inlineValuesBackground": "#000000",
            # "editor.inlineValuesForeground": "#000000",
            "editor.lineHighlightBackground": "#ffffff0A",
            "editor.lineHighlightBorder": self.background,
            # "editor.linkedEditingBackground": "#000000",
            # "editor.placeholder.foreground": "#000000",
            # "editor.rangeHighlightBackground": "#000000",
            # "editor.rangeHighlightBorder": "#000000",
            "editor.selectionBackground": self.accent + "99",
            "editor.selectionForeground": self.foreground_lighter,
            "editor.selectionHighlightBackground": self.accent + "99",
            "editor.selectionHighlightBorder": "#495F77",
            # "editor.snippetFinalTabstopHighlightBackground": "#000000",
            # "editor.snippetFinalTabstopHighlightBorder": "#000000",
            # "editor.snippetTabstopHighlightBackground": "#000000",
            # "editor.snippetTabstopHighlightBorder": "#000000",
            # "editor.stackFrameHighlightBackground": "#000000",
            # "editor.symbolHighlightBackground": "#000000",
            # "editor.symbolHighlightBorder": "#000000",
            "editor.wordHighlightBackground": "#55555599",
            # "editor.wordHighlightBorder": "#000000",
            "editor.wordHighlightStrongBackground": "#7d4200b8",
            # "editor.wordHighlightStrongBorder": "#000000",
            # "editor.wordHighlightTextBackground": "#000000",
            # "editor.wordHighlightTextBorder": "#000000",
            # "editorActionList.background": "#000000",
            # "editorActionList.focusBackground": "#000000",
            # "editorActionList.focusForeground": "#000000",
            # "editorActionList.foreground": "#000000",
            # "editorBracketHighlight.foreground1": "#000000",
            # "editorBracketHighlight.foreground2": "#000000",
            # "editorBracketHighlight.foreground3": "#000000",
            # "editorBracketHighlight.foreground4": "#000000",
            # "editorBracketHighlight.foreground5": "#000000",
            # "editorBracketHighlight.foreground6": "#000000",
            # "editorBracketHighlight.unexpectedBracket.foreground": "#000000",
            "editorBracketMatch.background": "#0064001a",
            "editorBracketMatch.border": "#888888",
            # "editorBracketPairGuide.activeBackground1": "#000000",
            # "editorBracketPairGuide.activeBackground2": "#000000",
            # "editorBracketPairGuide.activeBackground3": "#000000",
            # "editorBracketPairGuide.activeBackground4": "#000000",
            # "editorBracketPairGuide.activeBackground5": "#000000",
            # "editorBracketPairGuide.activeBackground6": "#000000",
            # "editorBracketPairGuide.background1": "#000000",
            # "editorBracketPairGuide.background2": "#000000",
            # "editorBracketPairGuide.background3": "#000000",
            # "editorBracketPairGuide.background4": "#000000",
            # "editorBracketPairGuide.background5": "#000000",
            # "editorBracketPairGuide.background6": "#000000",
            "editorCodeLens.foreground": "#777777",
            # "editorCommentsWidget.rangeActiveBackground": "#000000",
            # "editorCommentsWidget.rangeBackground": "#000000",
            # "editorCommentsWidget.replyInputBackground": "#000000",
            # "editorCommentsWidget.resolvedBorder": "#000000",
            # "editorCommentsWidget.unresolvedBorder": "#000000",
            "editorCursor.background": "#000000",
            "editorCursor.foreground": self.foreground,
            "editorError.background": "#B73A3400",
            "editorError.border": "#ffffff00",
            "editorError.foreground": "#f48771",
            # "editorGhostText.background": "#000000",
            # "editorGhostText.border": "#000000",
            # "editorGhostText.foreground": "#000000",
            "editorGroup.border": "#ffffff11",
            # "editorGroup.dropBackground": "#000000",
            # "editorGroup.dropIntoPromptBackground": "#000000",
            # "editorGroup.dropIntoPromptBorder": "#000000",
            # "editorGroup.dropIntoPromptForeground": "#000000",
            "editorGroup.emptyBackground": self.background_darker,
            # "editorGroup.focusedEmptyBorder": "#000000",
            "editorGroupHeader.border": self.border,
            # "editorGroupHeader.noTabsBackground": "#000000",
            "editorGroupHeader.tabsBackground": self.background_darker,
            # "editorGroupHeader.tabsBorder": "#000000",
            "editorGutter.addedBackground": "#587c0c",
            "editorGutter.background": "#20212699",
            # "editorGutter.commentGlyphForeground": "#000000",
            "editorGutter.commentRangeForeground": "#c5c5c5",
            # "editorGutter.commentUnresolvedGlyphForeground": "#000000",
            "editorGutter.deletedBackground": "#94151b",
            "editorGutter.foldingControlForeground": "#999999",
            # "editorGutter.itemBackground": "#000000",
            # "editorGutter.itemGlyphForeground": "#000000",
            # "editorGutter.modifiedBackground": "#0c7d9d",
            # "editorHint.border": "#000000",
            # "editorHint.foreground": "#000000",
            "editorHoverWidget.background": self.background,
            "editorHoverWidget.border": self.border,
            "editorHoverWidget.foreground": self.foreground,
            # "editorHoverWidget.highlightForeground": "#000000",
            # "editorHoverWidget.statusBarBackground": "#000000",
            # "editorIndentGuide.activeBackground1": "#000000",
            # "editorIndentGuide.activeBackground2": "#000000",
            # "editorIndentGuide.activeBackground3": "#000000",
            # "editorIndentGuide.activeBackground4": "#000000",
            # "editorIndentGuide.activeBackground5": "#000000",
            # "editorIndentGuide.activeBackground6": "#000000",
            # "editorIndentGuide.background1": "#000000",
            # "editorIndentGuide.background2": "#000000",
            # "editorIndentGuide.background3": "#000000",
            # "editorIndentGuide.background4": "#000000",
            # "editorIndentGuide.background5": "#000000",
            # "editorIndentGuide.background6": "#000000",
            "editorInfo.background": "#4490BF00",
            "editorInfo.border": "#4490BF00",
            "editorInfo.foreground": "#75beff",
            # "editorInlayHint.background": "#000000",
            # "editorInlayHint.foreground": "#000000",
            # "editorInlayHint.parameterBackground": "#000000",
            # "editorInlayHint.parameterForeground": "#000000",
            # "editorInlayHint.typeBackground": "#000000",
            # "editorInlayHint.typeForeground": "#000000",
            # "editorLightBulb.foreground": "#000000",
            # "editorLightBulbAi.foreground": "#000000",
            # "editorLightBulbAutoFix.foreground": "#000000",
            "editorLineNumber.activeForeground": self.foreground_lighter,
            "editorLineNumber.dimmedForeground": self.foreground_darker,
            "editorLineNumber.foreground": self.foreground,
            "editorLink.activeForeground": self.accent_lighter,
            "editorMarkerNavigation.background": "#2d2d30",
            "editorMarkerNavigationError.background": "#f48771",
            # "editorMarkerNavigationError.headerBackground": "#000000",
            "editorMarkerNavigationInfo.background": "#75beff",
            # "editorMarkerNavigationInfo.headerBackground": "#000000",
            "editorMarkerNavigationWarning.background": "#cca700",
            # "editorMarkerNavigationWarning.headerBackground": "#000000",
            # "editorMinimap.inlineChatInserted": "#000000",
            # "editorMultiCursor.primary.background": "#000000",
            # "editorMultiCursor.primary.foreground": "#000000",
            # "editorMultiCursor.secondary.background": "#000000",
            # "editorMultiCursor.secondary.foreground": "#000000",
            # "editorOverviewRuler.addedForeground": "#000000",
            # "editorOverviewRuler.background": "#000000",
            # "editorOverviewRuler.border": "#000000",
            # "editorOverviewRuler.bracketMatchForeground": "#000000",
            # "editorOverviewRuler.commentForeground": "#000000",
            # "editorOverviewRuler.commentUnresolvedForeground": "#000000",
            # "editorOverviewRuler.commonContentForeground": "#000000",
            # "editorOverviewRuler.currentContentForeground": "#000000",
            # "editorOverviewRuler.deletedForeground": "#000000",
            # "editorOverviewRuler.errorForeground": "#000000",
            # "editorOverviewRuler.findMatchForeground": "#000000",
            # "editorOverviewRuler.incomingContentForeground": "#000000",
            # "editorOverviewRuler.infoForeground": "#000000",
            # "editorOverviewRuler.inlineChatInserted": "#000000",
            # "editorOverviewRuler.inlineChatRemoved": "#000000",
            # "editorOverviewRuler.modifiedForeground": "#000000",
            # "editorOverviewRuler.rangeHighlightForeground": "#000000",
            # "editorOverviewRuler.selectionHighlightForeground": "#000000",
            # "editorOverviewRuler.warningForeground": "#000000",
            # "editorOverviewRuler.wordHighlightForeground": "#000000",
            # "editorOverviewRuler.wordHighlightStrongForeground": "#000000",
            # "editorOverviewRuler.wordHighlightTextForeground": "#000000",
            # "editorPane.background": "#000000",
            "editorRuler.foreground": self.foreground_darker,
            # "editorStickyScroll.background": "#000000",
            # "editorStickyScroll.border": "#000000",
            # "editorStickyScroll.shadow": "#000000",
            # "editorStickyScrollHover.background": "#000000",
            "editorSuggestWidget.background": self.background,
            "editorSuggestWidget.border": "#454545",
            "editorSuggestWidget.focusHighlightForeground": self.accent_lighter,
            "editorSuggestWidget.foreground": self.foreground,
            "editorSuggestWidget.highlightForeground": self.accent_lighter,
            "editorSuggestWidget.selectedBackground": self.accent,
            "editorSuggestWidget.selectedForeground": self.foreground,
            "editorSuggestWidget.selectedIconForeground": self.foreground,
            "editorSuggestWidgetStatus.foreground": self.foreground,
            # "editorUnicodeHighlight.background": "#000000",
            # "editorUnicodeHighlight.border": "#000000",
            # "editorUnnecessaryCode.border": "#000000",
            # "editorUnnecessaryCode.opacity": "#000000",
            "editorWarning.background": "#A9904000",
            "editorWarning.border": "#ffffff00",
            "editorWarning.foreground": "#cca700",
            "editorWatermark.foreground": "#000000",
            "editorWhitespace.foreground": self.foreground_darker,
            "editorWidget.background": self.background,
            "editorWidget.border": self.border,
            "editorWidget.foreground": self.foreground,
            "editorWidget.resizeBorder": "#5F5F5F",
        }

    def errorColors(self):
        return {
            # "errorForeground": "#000000",
            # "errorLens.errorBackground": "#000000",
            # "errorLens.errorBackgroundLight": "#000000",
            # "errorLens.errorForeground": "#000000",
            # "errorLens.errorForegroundLight": "#000000",
            # "errorLens.errorMessageBackground": "#000000",
            # "errorLens.errorRangeBackground": "#000000",
            # "errorLens.hintBackground": "#000000",
            # "errorLens.hintBackgroundLight": "#000000",
            # "errorLens.hintForeground": "#000000",
            # "errorLens.hintForegroundLight": "#000000",
            # "errorLens.hintMessageBackground": "#000000",
            # "errorLens.hintRangeBackground": "#000000",
            # "errorLens.infoBackground": "#000000",
            # "errorLens.infoBackgroundLight": "#000000",
            # "errorLens.infoForeground": "#000000",
            # "errorLens.infoForegroundLight": "#000000",
            # "errorLens.infoMessageBackground": "#000000",
            # "errorLens.infoRangeBackground": "#000000",
            # "errorLens.statusBarErrorForeground": "#000000",
            # "errorLens.statusBarHintForeground": "#000000",
            # "errorLens.statusBarIconErrorForeground": "#000000",
            # "errorLens.statusBarIconWarningForeground": "#000000",
            # "errorLens.statusBarInfoForeground": "#000000",
            # "errorLens.statusBarWarningForeground": "#000000",
            # "errorLens.warningBackground": "#000000",
            # "errorLens.warningBackgroundLight": "#000000",
            # "errorLens.warningForeground": "#000000",
            # "errorLens.warningForegroundLight": "#000000",
            # "errorLens.warningMessageBackground": "#000000",
            # "errorLens.warningRangeBackground": "#000000",
        }

    def extensionColors(self):
        return {
            # "extensionBadge.remoteBackground": "#000000",
            # "extensionBadge.remoteForeground": "#000000",
            # "extensionButton.background": "#000000",
            # "extensionButton.foreground": "#000000",
            # "extensionButton.hoverBackground": "#000000",
            # "extensionButton.prominentBackground": "#000000",
            # "extensionButton.prominentForeground": "#000000",
            # "extensionButton.prominentHoverBackground": "#000000",
            # "extensionButton.separator": "#000000",
            # "extensionIcon.preReleaseForeground": "#000000",
            # "extensionIcon.privateForeground": "#000000",
            # "extensionIcon.sponsorForeground": "#000000",
            # "extensionIcon.starForeground": "#000000",
            # "extensionIcon.verifiedForeground": "#000000",
        }

    def gaugeColors(self):
        return {
            # "gauge.background": "#000000",
            # "gauge.border": "#000000",
            # "gauge.errorBackground": "#000000",
            # "gauge.errorForeground": "#000000",
            # "gauge.foreground": "#000000",
            # "gauge.warningBackground": "#000000",
            # "gauge.warningForeground": "#000000",
        }

    def generalColors(self):
        return {
            "focusBorder": self.background_darker,
            "foreground": self.foreground,
            "icon.foreground": self.foreground,
        }

    def gitColors(self):
        return {
            # "git.blame.editorDecorationForeground": "#000000",
            "gitDecoration.addedResourceForeground": "#d4f5d999",
            "gitDecoration.conflictingResourceForeground": "#6c6cc4",
            "gitDecoration.deletedResourceForeground": "#99666699",
            "gitDecoration.ignoredResourceForeground": "#555555",
            "gitDecoration.modifiedResourceForeground": "#AA5800",
            # "gitDecoration.renamedResourceForeground": "#000000",
            "gitDecoration.stageDeletedResourceForeground": "#996666",
            "gitDecoration.stageModifiedResourceForeground": "#EC7900",
            "gitDecoration.submoduleResourceForeground": "#8de8a4",
            "gitDecoration.untrackedResourceForeground": "#cccccc",
        }

    def inlineColors(self):
        return {
            # "inlineChat.background": "#000000",
            # "inlineChat.border": "#000000",
            # "inlineChat.foreground": "#000000",
            # "inlineChat.shadow": "#000000",
            # "inlineChatDiff.inserted": "#000000",
            # "inlineChatDiff.removed": "#000000",
            # "inlineChatInput.background": "#000000",
            # "inlineChatInput.border": "#000000",
            # "inlineChatInput.focusBorder": "#000000",
            # "inlineChatInput.placeholderForeground": "#000000",
            # "inlineEdit.gutterIndicator.background": "#000000",
            # "inlineEdit.gutterIndicator.primaryBackground": "#000000",
            # "inlineEdit.gutterIndicator.primaryBorder": "#000000",
            # "inlineEdit.gutterIndicator.primaryForeground": "#000000",
            # "inlineEdit.gutterIndicator.secondaryBackground": "#000000",
            # "inlineEdit.gutterIndicator.secondaryBorder": "#000000",
            # "inlineEdit.gutterIndicator.secondaryForeground": "#000000",
            # "inlineEdit.gutterIndicator.successfulBackground": "#000000",
            # "inlineEdit.gutterIndicator.successfulBorder": "#000000",
            # "inlineEdit.gutterIndicator.successfulForeground": "#000000",
            # "inlineEdit.modifiedBackground": "#000000",
            # "inlineEdit.modifiedBorder": "#000000",
            # "inlineEdit.modifiedChangedLineBackground": "#000000",
            # "inlineEdit.modifiedChangedTextBackground": "#000000",
            # "inlineEdit.originalBackground": "#000000",
            # "inlineEdit.originalBorder": "#000000",
            # "inlineEdit.originalChangedLineBackground": "#000000",
            # "inlineEdit.originalChangedTextBackground": "#000000",
            # "inlineEdit.tabWillAcceptModifiedBorder": "#000000",
            # "inlineEdit.tabWillAcceptOriginalBorder": "#000000",
        }

    def inputColors(self):
        return {
            "input.background": self.background_lighter,
            "input.border": self.border + "00",
            "input.foreground": self.foreground,
            "input.placeholderForeground": "#a6a6a6",
        }

    def inputOptionColors(self):
        return {
            "inputOption.activeBackground": "#fc9320b9",
            "inputOption.activeBorder": "#007acc00",
            "inputOption.activeForeground": self.foreground_lighter,
            # "inputOption.hoverBackground": "#000000",
        }

    def inputValidationColors(self):
        return {
            # "inputValidation.errorBackground": "#000000",
            # "inputValidation.errorBorder": "#000000",
            # "inputValidation.errorForeground": "#000000",
            # "inputValidation.infoBackground": "#000000",
            # "inputValidation.infoBorder": "#000000",
            # "inputValidation.infoForeground": "#000000",
            # "inputValidation.warningBackground": "#000000",
            # "inputValidation.warningBorder": "#000000",
            # "inputValidation.warningForeground": "#000000",
        }

    def interactiveColors(self):
        return {
            # "interactive.activeCodeBorder": "#000000",
            # "interactive.inactiveCodeBorder": "#000000",
        }

    def issuesColors(self):
        return {
            # "issues.closed": "#000000",
            # "issues.newIssueDecoration": "#000000",
            # "issues.open": "#000000",
        }

    def keyBindingColors(self):
        return {
            # "keybindingLabel.background": "#000000",
            # "keybindingLabel.border": "#000000",
            # "keybindingLabel.bottomBorder": "#000000",
            # "keybindingLabel.foreground": "#000000",
            # "keybindingTable.headerBackground": "#000000",
            # "keybindingTable.rowsBackground": "#000000",
        }

    def listColors(self):
        return {
            "list.activeSelectionBackground": self.accent,
            "list.activeSelectionForeground": self.foreground_lighter,
            "list.activeSelectionIconForeground": self.foreground_lighter,
            # "list.deemphasizedForeground": "#000000",
            "list.dropBackground": self.background,
            "list.dropBetweenBackground": "#000000",
            "list.errorForeground": self.foreground,
            # "list.filterMatchBackground": "#000000",
            # "list.filterMatchBorder": "#000000",
            "list.focusAndSelectionOutline": self.accent_lighter,
            "list.focusBackground": self.accent,
            "list.focusForeground": self.foreground,
            "list.focusHighlightForeground": self.foreground_lighter,
            "list.focusOutline": self.accent_tertiary,
            "list.highlightForeground": self.foreground_lighter,
            "list.hoverBackground": self.background_lighter,
            "list.hoverForeground": self.foreground,
            "list.inactiveFocusBackground": self.background_lighter,
            "list.inactiveFocusOutline": self.background_darker,
            "list.inactiveSelectionBackground": self.background_darker,
            "list.inactiveSelectionForeground": self.foreground,
            "list.inactiveSelectionIconForeground": self.foreground,
            # "list.invalidItemForeground": "#000000",
            # "list.warningForeground": "#000000",
            "listFilterWidget.background": self.accent_lighter,
            "listFilterWidget.noMatchesOutline": "#be1100",
            "listFilterWidget.outline": "#00000000",
            "listFilterWidget.shadow": self.border,
        }

    def menuColors(self):
        return {
            "menu.background": self.background,
            "menu.border": self.border,
            "menu.foreground": self.foreground,
            "menu.selectionBackground": self.accent,
            "menu.selectionBorder": self.accent_lighter,
            "menu.selectionForeground": self.foreground,
            "menu.separatorBackground": self.foreground_darker,
            "menubar.selectionBackground": self.accent_lighter,
            "menubar.selectionBorder": self.accent,
            "menubar.selectionForeground": self.foreground_lighter,
        }

    def mergeColors(self):
        return {
            # "merge.border": "#000000",
            "merge.commonContentBackground": "#28282899",
            "merge.commonHeaderBackground": "#38383899",
            "merge.currentContentBackground": "#27403B99",
            "merge.currentHeaderBackground": "#36736699",
            "merge.incomingContentBackground": "#28384B99",
            "merge.incomingHeaderBackground": "#395F8F99",
            # "mergeEditor.change.background": "#000000",
            # "mergeEditor.change.word.background": "#000000",
            # "mergeEditor.changeBase.background": "#000000",
            # "mergeEditor.changeBase.word.background": "#000000",
            # "mergeEditor.conflict.handled.minimapOverViewRuler": "#000000",
            # "mergeEditor.conflict.handledFocused.border": "#000000",
            # "mergeEditor.conflict.handledUnfocused.border": "#000000",
            # "mergeEditor.conflict.input1.background": "#000000",
            # "mergeEditor.conflict.input2.background": "#000000",
            # "mergeEditor.conflict.unhandled.minimapOverViewRuler": "#000000",
            # "mergeEditor.conflict.unhandledFocused.border": "#000000",
            # "mergeEditor.conflict.unhandledUnfocused.border": "#000000",
            # "mergeEditor.conflictingLines.background": "#000000",
        }

    def minimapColors(self):
        return {
            "minimap.background": self.background,
            # "minimap.chatEditHighlight": "#000000",
            "minimap.errorHighlight": "#f48771",
            "minimap.findMatchHighlight": "#515c6a66",
            # "minimap.foregroundOpacity": "#000000",
            # "minimap.infoHighlight": "#000000",
            "minimap.selectionHighlight": "#55555599",
            # "minimap.selectionOccurrenceHighlight": "#000000",
            "minimap.warningHighlight": "#cca700",
            "minimapGutter.addedBackground": "#587c0c",
            "minimapGutter.deletedBackground": "#94151b",
            "minimapGutter.modifiedBackground": "#0c7d9d",
            # "minimapSlider.activeBackground": "#000000",
            # "minimapSlider.background": "#000000",
            # "minimapSlider.hoverBackground": "#000000",
        }

    def multiDiffEditorColors(self):
        return {
            # "multiDiffEditor.background": "#000000",
            # "multiDiffEditor.border": "#000000",
            # "multiDiffEditor.headerBackground": "#000000",
        }

    def notebookColors(self):
        return {
            # "notebook.cellBorderColor": "#000000",
            # "notebook.cellEditorBackground": "#000000",
            # "notebook.cellHoverBackground": "#000000",
            # "notebook.cellInsertionIndicator": "#000000",
            # "notebook.cellStatusBarItemHoverBackground": "#000000",
            # "notebook.cellToolbarSeparator": "#000000",
            # "notebook.editorBackground": "#000000",
            # "notebook.focusedCellBackground": "#000000",
            # "notebook.focusedCellBorder": "#000000",
            # "notebook.focusedEditorBorder": "#000000",
            # "notebook.inactiveFocusedCellBorder": "#000000",
            # "notebook.inactiveSelectedCellBorder": "#000000",
            # "notebook.outputContainerBackgroundColor": "#000000",
            # "notebook.outputContainerBorderColor": "#000000",
            # "notebook.selectedCellBackground": "#000000",
            # "notebook.selectedCellBorder": "#000000",
            # "notebook.symbolHighlightBackground": "#000000",
            # "notebookEditorOverviewRuler.runningCellForeground": "#000000",
            # "notebookScrollbarSlider.activeBackground": "#000000",
            # "notebookScrollbarSlider.background": "#000000",
            # "notebookScrollbarSlider.hoverBackground": "#000000",
            # "notebookStatusErrorIcon.foreground": "#000000",
            # "notebookStatusRunningIcon.foreground": "#000000",
            # "notebookStatusSuccessIcon.foreground": "#000000",
        }

    def notificationsColors(self):
        return {
            "notificationCenter.border": self.background_lighter,
            "notificationCenterHeader.background": self.border_lighter,
            "notificationCenterHeader.foreground": self.foreground,
            "notificationLink.foreground": self.accent_lighter,
            "notifications.background": self.background,
            "notifications.border": self.border_lighter,
            "notifications.foreground": self.foreground,
            "notificationsErrorIcon.foreground": "#f48771",
            "notificationsInfoIcon.foreground": "#75beff",
            "notificationsWarningIcon.foreground": "#cca700",
            "notificationToast.border": self.background_lighter,
        }

    def outputViewColors(self):
        return {
            # "outputView.background": "#000000",
            # "outputViewStickyScroll.background": "#000000",
        }

    def panelColors(self):
        return {
            "panel.background": "#000000",
            "panel.border": "#55555599",
            # "panel.dropBackground": "#000000",
            # "panel.dropBorder": "#000000",
            # "panelInput.border": "#000000",
            "panelSection.border": "#80808059",
            # "panelSection.dropBackground": "#000000",
            # "panelSectionHeader.background": "#000000",
            # "panelSectionHeader.border": "#000000",
            # "panelSectionHeader.foreground": "#000000",
            # "panelStickyScroll.background": "#000000",
            # "panelStickyScroll.border": "#000000",
            # "panelStickyScroll.shadow": "#000000",
            "panelTitle.activeBorder": self.accent_lighter,
            "panelTitle.activeForeground": self.foreground_lighter,
            # "panelTitle.border": "#000000",
            "panelTitle.inactiveForeground": self.foreground_darker,
            # "panelTitleBadge.background": "#000000",
            # "panelTitleBadge.foreground": "#000000",
        }

    def peekViewColors(self):
        return {
            "peekView.border": "#AA5800",
            "peekViewEditor.background": "#001f33",
            "peekViewEditor.matchHighlightBackground": "#ff8f0099",
            "peekViewEditor.matchHighlightBorder": "#ee931e",
            "peekViewEditorGutter.background": "#001f33",
            # "peekViewEditorStickyScroll.background": "#000000",
            "peekViewResult.background": self.background,
            "peekViewResult.fileForeground": self.foreground_lighter,
            "peekViewResult.lineForeground": self.foreground,
            "peekViewResult.matchHighlightBackground": "#ea5c004d",
            "peekViewResult.selectionBackground": "#3399ff33",
            "peekViewResult.selectionForeground": self.foreground_lighter,
            "peekViewTitle.background": "#1e1e1e",
            "peekViewTitleDescription.foreground": "#ccccccb3",
            "peekViewTitleLabel.foreground": self.foreground_lighter,
        }

    def pickerGroupColors(self):
        return {
            "pickerGroup.border": self.background_lighter,
            "pickerGroup.foreground": self.accent_lighter,
        }

    def portsColors(self):
        return {
            # "ports.iconRunningProcessForeground": "#000000",
        }

    def problemsColors(self):
        return {
            # "problemsErrorIcon.foreground": "#000000",
            # "problemsInfoIcon.foreground": "#000000",
            # "problemsWarningIcon.foreground": "#000000",
        }

    def profileColors(self):
        return {
            # "profileBadge.background": "#000000",
            # "profileBadge.foreground": "#000000",
            # "profiles.sashBorder": "#000000",
        }

    def progressBarColors(self):
        return {
            "progressBar.background": self.accent_tertiary,
        }

    def pullRequestsColors(self):
        return {
            # "pullRequests.draft": "#000000",
            # "pullRequests.merged": "#000000",
            # "pullRequests.notification": "#000000",
            # "pullRequests.open": "#000000",
        }

    def quickInputColors(self):
        return {
            # "quickInput.background": "#000000",
            # "quickInput.foreground": "#000000",
            # "quickInputList.focusBackground": "#000000",
            # "quickInputList.focusForeground": "#000000",
            # "quickInputList.focusIconForeground": "#000000",
            # "quickInputTitle.background": "#000000",
        }

    def radioColors(self):
        return {
            # "radio.activeBackground": "#000000",
            # "radio.activeBorder": "#000000",
            # "radio.activeForeground": "#000000",
            # "radio.inactiveBackground": "#000000",
            # "radio.inactiveBorder": "#000000",
            # "radio.inactiveForeground": "#000000",
            # "radio.inactiveHoverBackground": "#000000",
        }

    def sashColors(self):
        return {
            # "sash.hoverBorder": "#000000",
        }

    def scmGraphColors(self):
        return {
            # "scmGraph.foreground1": "#000000",
            # "scmGraph.foreground2": "#000000",
            # "scmGraph.foreground3": "#000000",
            # "scmGraph.foreground4": "#000000",
            # "scmGraph.foreground5": "#000000",
            # "scmGraph.historyItemBaseRefColor": "#000000",
            # "scmGraph.historyItemHoverAdditionsForeground": "#000000",
            # "scmGraph.historyItemHoverDefaultLabelBackground": "#000000",
            # "scmGraph.historyItemHoverDefaultLabelForeground": "#000000",
            # "scmGraph.historyItemHoverDeletionsForeground": "#000000",
            # "scmGraph.historyItemHoverLabelForeground": "#000000",
            # "scmGraph.historyItemRefColor": "#000000",
            # "scmGraph.historyItemRemoteRefColor": "#000000",
        }

    def scrollBarColors(self):
        return {
            # "scrollbar.shadow": "#000000",
            "scrollbarSlider.activeBackground": "#bfbfbf66",
            "scrollbarSlider.background": "#79797966",
            "scrollbarSlider.hoverBackground": "#646464b3",
        }

    def searchColors(self):
        return {
            # "search.resultsInfoForeground": "#000000",
            # "searchEditor.findMatchBackground": "#000000",
            # "searchEditor.findMatchBorder": "#000000",
            # "searchEditor.textInputBorder": "#000000",
        }

    def selectionColors(self):
        return {
            "selection.background": self.accent,
        }

    def settingsColors(self):
        return {
            # "settings.checkboxBackground": "#000000",
            # "settings.checkboxBorder": "#000000",
            # "settings.checkboxForeground": "#000000",
            # "settings.dropdownBackground": "#000000",
            # "settings.dropdownBorder": "#000000",
            # "settings.dropdownForeground": "#000000",
            # "settings.dropdownListBorder": "#000000",
            "settings.focusedRowBackground": "#ffffff07",
            # "settings.focusedRowBorder": "#000000",
            # "settings.headerBorder": "#000000",
            "settings.headerForeground": self.foreground,
            # "settings.modifiedItemIndicator": "#000000",
            # "settings.numberInputBackground": "#000000",
            # "settings.numberInputBorder": "#000000",
            # "settings.numberInputForeground": "#000000",
            # "settings.rowHoverBackground": "#000000",
            # "settings.sashBorder": "#000000",
            # "settings.settingsHeaderHoverForeground": "#000000",
            # "settings.textInputBackground": "#000000",
            # "settings.textInputBorder": "#000000",
            # "settings.textInputForeground": "#000000",
        }

    def sideBarColors(self):
        return {
            "sideBar.background": self.background_darker,
            "sideBar.border": self.border,
            "sideBar.dropBackground": self.background_lighter,
            "sideBar.foreground": self.foreground,
            "sideBarActivityBarTop.border": "#000000",
            "sideBarSectionHeader.background": "#00000000",
            "sideBarSectionHeader.border": "#55555566",
            "sideBarSectionHeader.foreground": self.foreground,
            "sideBarStickyScroll.background": "#000000",
            "sideBarStickyScroll.border": "#000000",
            "sideBarStickyScroll.shadow": "#000000",
            "sideBarTitle.background": self.background,
            "sideBarTitle.border": self.border,
            "sideBarTitle.foreground": self.foreground_lighter,
            # "sideBySideEditor.horizontalBorder": "#000000",
            # "sideBySideEditor.verticalBorder": "#000000",
            "simpleFindWidget.sashBorder": "#000000",
        }

    def statusBarColors(self):
        return {
            "statusBar.background": self.background,
            "statusBar.border": self.border,
            "statusBar.debuggingBackground": self.accent,
            "statusBar.debuggingBorder": "#000000",
            "statusBar.debuggingForeground": self.foreground_lighter,
            "statusBar.focusBorder": self.foreground_darker,
            "statusBar.foreground": self.foreground,
            "statusBar.noFolderBackground": self.background,
            "statusBar.noFolderBorder": self.border,
            "statusBar.noFolderForeground": self.foreground_lighter,
            "statusBarItem.activeBackground": "#FFFFFF25",
            # "statusBarItem.compactHoverBackground": "#000000",
            # "statusBarItem.errorBackground": "#000000",
            # "statusBarItem.errorForeground": "#000000",
            # "statusBarItem.errorHoverBackground": "#000000",
            # "statusBarItem.errorHoverForeground": "#000000",
            # "statusBarItem.focusBorder": "#000000",
            "statusBarItem.hoverBackground": "#ffffff1f",
            # "statusBarItem.hoverForeground": "#000000",
            # "statusBarItem.offlineBackground": "#000000",
            # "statusBarItem.offlineForeground": "#000000",
            # "statusBarItem.offlineHoverBackground": "#000000",
            # "statusBarItem.offlineHoverForeground": "#000000",
            # "statusBarItem.prominentBackground": "#000000",
            # "statusBarItem.prominentForeground": "#000000",
            # "statusBarItem.prominentHoverBackground": "#000000",
            # "statusBarItem.prominentHoverForeground": "#000000",
            "statusBarItem.remoteBackground": self.accent,
            "statusBarItem.remoteForeground": self.foreground_lighter,
            "statusBarItem.remoteHoverBackground": self.accent_lighter,
            "statusBarItem.remoteHoverForeground": self.foreground_lighter,
            # "statusBarItem.warningBackground": "#000000",
            # "statusBarItem.warningForeground": "#000000",
            # "statusBarItem.warningHoverBackground": "#000000",
            # "statusBarItem.warningHoverForeground": "#000000",
        }

    def symbolIconsColors(self):
        return {
            # "symbolIcon.arrayForeground": "#000000",
            # "symbolIcon.booleanForeground": "#000000",
            # "symbolIcon.classForeground": "#000000",
            # "symbolIcon.colorForeground": "#000000",
            # "symbolIcon.constantForeground": "#000000",
            # "symbolIcon.constructorForeground": "#000000",
            # "symbolIcon.enumeratorForeground": "#000000",
            # "symbolIcon.enumeratorMemberForeground": "#000000",
            # "symbolIcon.eventForeground": "#000000",
            # "symbolIcon.fieldForeground": "#000000",
            # "symbolIcon.fileForeground": "#000000",
            # "symbolIcon.folderForeground": "#000000",
            # "symbolIcon.functionForeground": "#000000",
            # "symbolIcon.interfaceForeground": "#000000",
            # "symbolIcon.keyForeground": "#000000",
            # "symbolIcon.keywordForeground": "#000000",
            # "symbolIcon.methodForeground": "#000000",
            # "symbolIcon.moduleForeground": "#000000",
            # "symbolIcon.namespaceForeground": "#000000",
            # "symbolIcon.nullForeground": "#000000",
            # "symbolIcon.numberForeground": "#000000",
            # "symbolIcon.objectForeground": "#000000",
            # "symbolIcon.operatorForeground": "#000000",
            # "symbolIcon.packageForeground": "#000000",
            # "symbolIcon.propertyForeground": "#000000",
            # "symbolIcon.referenceForeground": "#000000",
            # "symbolIcon.snippetForeground": "#000000",
            # "symbolIcon.stringForeground": "#000000",
            # "symbolIcon.structForeground": "#000000",
            # "symbolIcon.textForeground": "#000000",
            # "symbolIcon.typeParameterForeground": "#000000",
            # "symbolIcon.unitForeground": "#000000",
            # "symbolIcon.variableForeground": "#000000",
        }

    def tabColors(self):
        return {
            "tab.activeBackground": self.background,
            "tab.activeBorder": "#00000000",
            "tab.activeBorderTop": self.accent_lighter,
            "tab.activeForeground": self.foreground,
            # "tab.activeModifiedBorder": "#000000",
            "tab.border": self.background,
            # "tab.dragAndDropBorder": "#000000",
            "tab.hoverBackground": self.background,
            "tab.hoverBorder": self.background,
            "tab.hoverForeground": self.foreground_lighter,
            "tab.inactiveBackground": self.background_darker,
            "tab.inactiveForeground": "#ffffff80",
            # "tab.inactiveModifiedBorder": "#000000",
            # "tab.lastPinnedBorder": "#000000",
            # "tab.selectedBackground": "#000000",
            # "tab.selectedBorderTop": "#000000",
            # "tab.selectedForeground": "#000000",
            # "tab.unfocusedActiveBackground": "#000000",
            # "tab.unfocusedActiveBorder": "#000000",
            # "tab.unfocusedActiveBorderTop": "#000000",
            # "tab.unfocusedActiveForeground": "#000000",
            # "tab.unfocusedActiveModifiedBorder": "#000000",
            # "tab.unfocusedHoverBackground": "#000000",
            # "tab.unfocusedHoverBorder": "#000000",
            # "tab.unfocusedHoverForeground": "#000000",
            # "tab.unfocusedInactiveForeground": "#000000",
            # "tab.unfocusedInactiveModifiedBorder": "#000000",
        }

    def terminalColors(self):
        return {
            "terminal.ansiBlack": "#000000",
            "terminal.ansiBlue": "#2472c8",
            "terminal.ansiBrightBlack": "#666666",
            "terminal.ansiBrightBlue": "#3b8eea",
            "terminal.ansiBrightCyan": "#29b8db",
            "terminal.ansiBrightGreen": "#23d18b",
            "terminal.ansiBrightMagenta": "#d670d6",
            "terminal.ansiBrightRed": "#f14c4c",
            "terminal.ansiBrightWhite": "#e5e5e5",
            "terminal.ansiBrightYellow": "#f5f543",
            "terminal.ansiCyan": "#11a8cd",
            "terminal.ansiGreen": "#0dbc79",
            "terminal.ansiMagenta": "#bc3fbc",
            "terminal.ansiRed": "#cd3131",
            "terminal.ansiWhite": "#e5e5e5",
            "terminal.ansiYellow": "#e5e510",
            "terminal.background": "#000000",
            "terminal.border": "#80808059",
            # "terminal.dropBackground": "#000000",
            # "terminal.findMatchBackground": "#000000",
            # "terminal.findMatchBorder": "#000000",
            # "terminal.findMatchHighlightBackground": "#000000",
            # "terminal.findMatchHighlightBorder": "#000000",
            "terminal.foreground": self.foreground,
            # "terminal.hoverHighlightBackground": "#000000",
            # "terminal.inactiveSelectionBackground": "#000000",
            # "terminal.initialHintForeground": "#000000",
            # "terminal.selectionBackground": "#000000",
            # "terminal.selectionForeground": "#000000",
            # "terminal.tab.activeBorder": "#000000",
            # "terminalCommandDecoration.defaultBackground": "#000000",
            # "terminalCommandDecoration.errorBackground": "#000000",
            # "terminalCommandDecoration.successBackground": "#000000",
            # "terminalCommandGuide.foreground": "#000000",
            "terminalCursor.background": "#fc9320",
            "terminalCursor.foreground": self.foreground_lighter,
            # "terminalOverviewRuler.border": "#000000",
            # "terminalOverviewRuler.cursorForeground": "#000000",
            # "terminalOverviewRuler.findMatchForeground": "#000000",
            # "terminalStickyScroll.background": "#000000",
            # "terminalStickyScroll.border": "#000000",
            # "terminalStickyScrollHover.background": "#000000",
            # "terminalSymbolIcon.aliasForeground": "#000000",
            # "terminalSymbolIcon.argumentForeground": "#000000",
            # "terminalSymbolIcon.fileForeground": "#000000",
            # "terminalSymbolIcon.flagForeground": "#000000",
            # "terminalSymbolIcon.folderForeground": "#000000",
            # "terminalSymbolIcon.inlineSuggestionForeground": "#000000",
            # "terminalSymbolIcon.methodForeground": "#000000",
            # "terminalSymbolIcon.optionForeground": "#000000",
            # "terminalSymbolIcon.optionValueForeground": "#000000",
        }

    def testingColors(self):
        return {
            # "testing.coverCountBadgeBackground": "#000000",
            # "testing.coverCountBadgeForeground": "#000000",
            # "testing.coveredBackground": "#000000",
            # "testing.coveredBorder": "#000000",
            # "testing.coveredGutterBackground": "#000000",
            # "testing.iconErrored": "#000000",
            # "testing.iconErrored.retired": "#000000",
            # "testing.iconFailed": "#000000",
            # "testing.iconFailed.retired": "#000000",
            # "testing.iconPassed": "#000000",
            # "testing.iconPassed.retired": "#000000",
            # "testing.iconQueued": "#000000",
            # "testing.iconQueued.retired": "#000000",
            # "testing.iconSkipped": "#000000",
            # "testing.iconSkipped.retired": "#000000",
            # "testing.iconUnset": "#000000",
            # "testing.iconUnset.retired": "#000000",
            # "testing.message.error.badgeBackground": "#000000",
            # "testing.message.error.badgeBorder": "#000000",
            # "testing.message.error.badgeForeground": "#000000",
            # "testing.message.error.lineBackground": "#000000",
            # "testing.message.info.decorationForeground": "#000000",
            # "testing.message.info.lineBackground": "#000000",
            # "testing.messagePeekBorder": "#000000",
            # "testing.messagePeekHeaderBackground": "#000000",
            # "testing.peekBorder": "#000000",
            # "testing.peekHeaderBackground": "#000000",
            # "testing.runAction": "#000000",
            # "testing.uncoveredBackground": "#000000",
            # "testing.uncoveredBorder": "#000000",
            # "testing.uncoveredBranchBackground": "#000000",
            # "testing.uncoveredGutterBackground": "#000000",
        }

    def textColors(self):
        return {
            # "textBlockQuote.background": "#000000",
            # "textBlockQuote.border": "#000000",
            # "textCodeBlock.background": "#000000",
            "textLink.activeForeground": self.accent_lighter,
            "textLink.foreground": self.accent,
            # "textPreformat.background": "#000000",
            # "textPreformat.foreground": "#000000",
            "textSeparator.foreground": self.foreground_darker,
        }

    def titleBarColors(self):
        return {
            "titleBar.activeBackground": self.background,
            "titleBar.activeForeground": self.foreground_lighter,
            "titleBar.border": self.border,
            "titleBar.inactiveBackground": self.background_darker,
            "titleBar.inactiveForeground": self.foreground,
        }

    def toolbarColors(self):
        return {
            # "toolbar.activeBackground": "#000000",
            # "toolbar.hoverBackground": "#000000",
            # "toolbar.hoverOutline": "#000000",
        }

    def treeColors(self):
        return {
            # "tree.inactiveIndentGuidesStroke": "#000000",
            "tree.indentGuidesStroke": self.foreground_darker,
            # "tree.tableColumnsBorder": "#000000",
            # "tree.tableOddRowsBackground": "#000000",
        }

    def walkThroughColors(self):
        return {
            "walkThrough.embeddedEditorBackground": "#00000050",
            # "walkthrough.stepTitle.foreground": "#000000",
        }

    def welcomePageColors(self):
        return {
            # "welcomePage.background": "#000000",
            # "welcomePage.progress.background": "#000000",
            # "welcomePage.progress.foreground": "#000000",
            # "welcomePage.tileBackground": "#000000",
            # "welcomePage.tileBorder": "#000000",
            # "welcomePage.tileHoverBackground": "#000000",
        }

    def widgetColors(self):
        return {
            # "widget.border": "#000000",
            # "widget.shadow": "#000000",
        }

    def windowColors(self):
        return {
            "window.activeBorder": self.background_darker, 
            "window.inactiveBorder": self.border_darker
        }
